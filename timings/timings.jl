module Timings

using ValueNoise
using CorrelationFunctions
using Statistics
using DelimitedFiles

getdata(side, :: Val{2}) =
    [value_noise(3x/side, 3y/side, 0.0, 4, 34365) < 0.5 for x in 1:side, y in 1:side]

getdata(side, :: Val{3}) =
    [value_noise(3x/side, 3y/side, 3z/side, 4, 34365) < 0.5 for x in 1:side, y in 1:side, z in 1:side]

const data_2d = (getdata(side, Val(2)) for side in 1000:1000:6000)
const data_3d = (getdata(side, Val(3)) for side in 50:50:300)

fst((x, _)) = x
snd((_, y)) = y

function calculate_time!(fn, dim, prefix)
    data_arrays = (dim == 2) ? data_2d : data_3d

    timings = map(data_arrays) do data
        side = size(data, 1)
        println(side)
        time = let
            time = time_ns();
            fn(data, true; periodic = true);
            (time_ns() - time) / 10^9
        end
        (side, time)
    end

    res = hcat(fst.(timings), snd.(timings))
    open("$(fn)-$(prefix)-$(dim)d.dat", "w") do io
        writedlm(io, res)
    end
    
    return res
end

const fn_dir = [
    Directional.l2,
    Directional.s2,
    Directional.c2,
    Directional.surfsurf,
    Directional.surfvoid
]

function do_all!()
    foreach(fn -> calculate_time!(fn, 2, "directional"), fn_dir)
    foreach(fn -> calculate_time!(fn, 3, "directional"), fn_dir)
end

export do_all!
end
