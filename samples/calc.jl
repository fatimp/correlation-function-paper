module SomeShit

import CorrelationFunctions.Directional as D
import CorrelationFunctions.Utilities as U
using Statistics
using NPZ
using FileIO
using Images

const fns = [:s2, :l2, :c2, :surf2, :surfvoid]

#=
function read_files()
    rawfiles = filter(readdir(".")) do name
        splitext(name)[2] == ".raw"
    end

    return Iterators.map(rawfiles) do name
        (splitext(name)[1], U.read_cuboid(name, 1000, 3) |> BitArray)
    end
end
=#

function read_files()
    rawfiles = filter(readdir(".")) do name
        splitext(name)[2] == ".png"
    end

    return Iterators.map(rawfiles) do name
        (splitext(name)[1], name |> load .|> Gray |> BitArray)
    end
end

function do_it!()
    data = read_files()

    for (name, sample) in data
        println(name)
        for sym in fns
            fn = D.eval(sym)
            a = fn(sample, true; periodic = true) |> mean
            npzwrite("$(name)-$(sym).npy", a)
        end
    end
end

end
