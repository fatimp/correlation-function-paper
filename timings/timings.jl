using ValueNoise
using CorrelationFunctions
using Statistics
using DelimitedFiles

getdata(side, :: Val{2}) =
    [value_noise(5x/side, 5y/side, 0.0, 5, 34365) < 0.5 for x in 1:side, y in 1:side]

getdata(side, :: Val{3}) =
    [value_noise(5x/side, 5y/side, 5z/side, 5, 34365) < 0.5 for x in 1:side, y in 1:side, z in 1:side]

#const data_2d = [getdata(side, Val(2)) for side in 1000:1000:10000]
const data_3d = [getdata(side, Val(3)) for side in 50:50:500]

function calculate_time!(fn, dim)
    sides = Vector{Int}(undef, 0)
    times = Vector{Float64}(undef, 0)
    data_arrays = (dim == 2) ? data_2d : data_3d

    for data in data_arrays
        side = size(data, 1)
        push!(sides, side)
        println(side)
        #time = sum(let time = time_ns(); fn(data, 1); time_ns() - time end for i in 1:5) / 5
        time = sum(let time = time_ns(); fn(data, 1); time_ns() - time end for i in 1:2) / 2
        push!(times, time / 10^9)
    end

    res = hcat(sides, times)
    open("/home/vasily/timings/$(fn)-$(dim)d.dat", "w") do io
        writedlm(io, res)
    end
    
    return res
end
