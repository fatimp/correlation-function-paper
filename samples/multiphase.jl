module WTF
import CorrelationFunctions.Utilities as U
import CorrelationFunctions.Directional as D
using NPZ
using Statistics

function do_it!()
    data = U.read_cuboid("image3d_multi_4phases.raw", 304, 3)

    for (p1, p2) in [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (1, 2)]
        cc = D.cross_correlation(data, p1, p2; periodic = true)
        npzwrite("multiphase-$(p1)-$(p2).npy", mean(cc))
    end
end

end
