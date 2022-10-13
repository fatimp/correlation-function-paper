module Shit
using Distributions
using Statistics
using CorrelationFunctions
using DelimitedFiles
import Random

function gencenters(side, λ)
    n = (λ * side^3) |> Poisson |> rand
    return reduce(hcat, (rand(1:side, 3) for i in 1:n))
end

function genballs(side, R, λ)
    sphere_side = 2R + 1
    padded_side = side + sphere_side
    spheres = zeros(Int8, (padded_side, padded_side, padded_side))
    sphere = zeros(Int8, (sphere_side, sphere_side, sphere_side))
    centers = gencenters(side, λ)
    for i in -R:R
        for j in -R:R
            for k in -R:R
                dist = i^2 + j^2 + k^2
                if dist < R^2
                    sphere[k+R+1, j+R+1, i+R+1] = 1
                end
            end
        end
    end

    for center in (centers[:,i] for i in 1:size(centers,2))
        x = center[1]
        y = center[2]
        z = center[3]
        spheres[x:x + 2R, y:y + 2R, z:z + 2R] .|= sphere
    end
    return spheres[R+1:end-R-1, R+1:end-R-1, R+1:end-R-1]
end

s2_theory(r, R, λ) =
    let a = (r > 2R) ? 8/3*R^3 : (4/3*R^3 + r*R^2 - r^3/12);
        exp(-λ*π*a)
    end

ss_theory(r, R, λ) =
    let η = 4/3*λ*π*R^3;
        a = (r > 2R) ? 9η^2/R^2 : (9η^2/R^2*(1/2 + r/(4R))^2 + 3η/(2r*R))
        a*s2_theory(r, R, λ)
    end

sv_theory(r, R, λ) =
    let η = 4/3*λ*π*R^3;
        a = (r > 2R) ? 1 : (1/2 + r/(4R))
        3η/R*a*s2_theory(r, R, λ)
    end

l2_theory(r, R, λ) =
    exp(-λ*π * (4/3*R^3 + r*R^2))

cl_theory(r, R, λ) = π*λ*R^2*exp(-π*λ*r*R^2)

ps_theory(r, R, λ) = 4π*λ*(r + R)^2 * exp(-4/3*π*λ* (r^3 + 3r^2*R + 3r*R^2))

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
    side = 500
    R = 10
    λ = 1e-4

    Random.seed!(13435)
    data = genballs(side, R, λ)
    println(sum(data)/length(data))
    for (name, theory, impl) in fns
        calc = data |> impl |> mean
        th   = theory.(0:length(calc)-1, R, λ)
        open("$(name)-3d.dat", "w") do out
            writedlm(out, hcat(calc,th))
        end
    end
    Base.GC.gc()
    for (name, theory, impl) in hists
        calc = data |> impl
        xs = range(minimum(calc), maximum(calc), 1000)
        open("$(name)-3d-hist.dat", "w") do out
            writedlm(out, calc)
        end
        open("$(name)-3d-prob.dat", "w") do out
            writedlm(out, hcat(xs, theory.(xs, R, λ)))
        end
    end
end

end
