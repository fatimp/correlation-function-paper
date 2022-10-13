module Shit
using Distributions
using Statistics
using CorrelationFunctions
using DelimitedFiles
import Random

function gencenters(side, λ)
    n = (λ * side^2) |> Poisson |> rand
    return reduce(hcat, (rand(1:side, 2) for i in 1:n))
end

function gendisks(side, R, λ)
    spheres = zeros(Int8, (side + 2R + 1, side + 2R + 1))
    sphere  = zeros(Int8, (2R + 1, 2R + 1))
    centers = gencenters(side, λ)
    for i in -R:R
        for j in -R:R
            dist = i^2 + j^2
            if dist < R^2
                sphere[j+R+1, i+R+1] = 1
            end
        end
    end
    for center in (centers[:,i] for i in 1:size(centers,2))
        x = center[1]
        y = center[2]
        spheres[x:x + 2R, y:y + 2R] .|= sphere
    end
    return spheres[R+1:end-R-1, R+1:end-R-1]
end

s2_theory(r, R, λ) =
    let A = 4R^2 - r^2;
        a = (r < 2R) ? π*R^2 + r*sqrt(A)/4 - acos(r/(2R))*R^2 : π*R^2;
        exp(-2λ*a)
end

ss_theory(r, R, λ) =
    let A = 4R^2 - r^2;
        a = (r < 2R) ?
            (A*R^2*λ^2*r*(acos(r/(2R))^2 - 2π*acos(r/(2R)) + π^2) + sqrt(A)*R^2*λ)/(A*r) : (π*λ*R)^2
        4a*s2_theory(r, R, λ)
    end

sv_theory(r, R, λ) =
    let A = 4R^2 - r^2;
        a = (r < 2R) ? π - acos(r/(2R)) : π
        2R*λ*a*s2_theory(r, R, λ)
    end

l2_theory(r, R, λ) =
    exp(-λ*(π*R^2 + 2r*R))

cl_theory(r, R, λ) = 2λ*R*exp(-2λ*r*R)

ps_theory(r, R, λ) = 2λ*π*(r + R)*exp(-λ*π*(r^2 + 2r*R))

const fns = [
    ("s2", s2_theory,
     img -> Directional.s2(img, false; periodic = true)),
    ("l2", l2_theory,
     img -> Directional.l2(img, false; periodic = true)),
    ("ss", ss_theory,
     img -> Directional.surfsurf(img, false; periodic = true,
                                 edgemode = Utilities.EdgesFilterReflect())),
    ("sv", sv_theory,
     img -> Directional.surfvoid(img, false; periodic = true,
                                 edgemode = Utilities.EdgesFilterReflect()))
]

const hists = [
    # FIXME: Check pore_size
    ("pore_size", ps_theory,
     img -> Directional.pore_size(img, false; nbins = 20)),
    ("chord_length", cl_theory,
     img -> Directional.chord_length(img, false; nbins = 20))
]

function main!()
    side = 10000
    R = 40
    λ = 5e-5

    Random.seed!(13435)
    data = gendisks(side, R, λ)
    println(sum(data)/length(data))
    for (name, theory, impl) in fns
        calc = data |> impl |> mean
        th   = theory.(0:length(calc)-1, R, λ)
        open("$(name)-2d.dat", "w") do out
            writedlm(out, hcat(calc,th))
        end
    end
    Base.GC.gc()
    for (name, theory, impl) in hists
        calc = data |> impl
        xs = range(minimum(calc), maximum(calc), 1000)
        open("$(name)-2d-hist.dat", "w") do out
            writedlm(out, calc)
        end
        open("$(name)-2d-prob.dat", "w") do out
            writedlm(out, hcat(xs, theory.(xs, R, λ)))
        end
    end
end

end
