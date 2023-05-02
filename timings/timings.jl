module Timings

import CorrelationFunctions.Map as M
import CorrelationFunctions.Directional as D
import Statistics as S
import Distributions as Dist
using DelimitedFiles
using NPZ

function draw_balls(s)
    array = falses(s...)
    center1 = Iterators.repeated(0.3, length(s))
    center2 = Iterators.repeated(0.7, length(s))
    r = 0.2

    for idx in CartesianIndices(array)
        dist1 = sum((Tuple(idx) ./s .- center1) .^ 2)
        dist2 = sum((Tuple(idx) ./s .- center2) .^ 2)
        if dist1 <= r^2 || dist2 <= r^2
            array[idx] = true
        end
    end

    return array
end

function prepare!()
    for side in 1000:1000:6000
        println(side)
        balls = draw_balls((side, side))
        npzwrite("disks-$(side).npy", balls)
    end

    for side in 50:50:300
        println(side)
        balls = draw_balls((side, side, side))
        npzwrite("balls-$(side).npy", balls)
    end
end

fst((x, _)) = x
snd((_, y)) = y

struct FnSpec
    fn   :: Function
    name :: String
end

struct ExecResult
    side  :: Int
    mean  :: Float64
    range :: Float64
end

s(res :: ExecResult) = res.side
μ(res :: ExecResult) = res.mean
r(res :: ExecResult) = res.range

(fn :: FnSpec)(data) = fn.fn(data)

function estimate_range(array :: AbstractArray, prob)
    len = length(array)
    t = Dist.TDist(len - 1)
    # FIXME: quantile function is for one-tailed tests.
    # Recalculate `prob` from two-tailed to one-tailed
    α = 1 - prob
    return Dist.quantile(t, 1 - α/2) * S.std(array) / sqrt(len)
end

function calculate_time!(fn :: FnSpec, dim, prefix)
    println(fn.name)
    data_arrays = (dim == 2) ?
        ("disks-$(side).npy" for side in 1000:1000:6000) :
        ("balls-$(side).npy" for side in 50:50:300)

    # Make sure JIT is done
    data_arrays |> first |> npzread |> fn

    timings = map(data_arrays) do datapath
        data = npzread(datapath)
        side = size(data, 1)
        println(side)
        times = Float64[]
        while sum(times) < 10 || length(times) < 3
            atime = time_ns()
            fn(data)
            atime = (time_ns() - atime) / 10^9
            push!(times, atime)
        end
        ExecResult(side, S.mean(times), estimate_range(times, 0.9))
    end

    res = hcat(s.(timings), μ.(timings), r.(timings))
    open("$(fn.name)-$(prefix)-$(dim)d.dat", "w") do io
        writedlm(io, res)
    end
    
    return res
end

const fn_dir = [
    FnSpec(data -> D.chord_length(data, true), "chord_length"),
    FnSpec(data -> D.pore_size(data, true; periodic = true), "pore_size"),
    FnSpec(data -> D.l2(data, true; periodic = true), "l2"),
    FnSpec(data -> D.s2(data, true; periodic = true), "s2"),
    FnSpec(data -> D.c2(data, true; periodic = true), "c2"),
    FnSpec(data -> D.surf2(data, true; periodic = true), "surf2"),
    FnSpec(data -> D.surfvoid(data, true; periodic = true), "surfvoid")
]

function do_all!()
    foreach(fn -> calculate_time!(fn, 2, "directional"), fn_dir)
    foreach(fn -> calculate_time!(fn, 3, "directional"), fn_dir)
end

export do_all!, prepare!
end
