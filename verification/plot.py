#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

s2_2d = np.loadtxt('s2-2d.dat')
s2_3d = np.loadtxt('s2-3d.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(s2_2d[:, 0], 'r-', linewidth = 2.0)
plt.plot(s2_2d[:, 1], 'b-', linewidth = 2.0)
plt.plot(s2_3d[:, 0], 'r--', linewidth = 2.0)
plt.plot(s2_3d[:, 1], 'b--', linewidth = 2.0)
plt.xlim([0, 130])
plt.xlabel('Correlation length $r$')
plt.ylabel('Two point function $S_2(r)$')
plt.legend(['CorrelationFunctions.jl (2D)', 'Theory (2D)',
            'CorrelationFunctions.jl (3D)', 'Theory (3D)'])
plt.savefig('s2.png')

l2_2d = np.loadtxt('l2-2d.dat')
l2_3d = np.loadtxt('l2-3d.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(l2_2d[:, 0], 'r-', linewidth = 2.0)
plt.plot(l2_2d[:, 1], 'b-', linewidth = 2.0)
plt.plot(l2_3d[:, 0], 'r--', linewidth = 2.0)
plt.plot(l2_3d[:, 1], 'b--', linewidth = 2.0)
plt.xlim([0, 150])
plt.xlabel('Correlation length $r$')
plt.ylabel('Lineal-path function $L_2(r)$')
plt.legend(['CorrelationFunctions.jl (2D)', 'Theory (2D)',
            'CorrelationFunctions.jl (3D)', 'Theory (3D)'])
plt.savefig('l2.png')

ss_2d = np.loadtxt('ss-2d.dat')
ss_3d = np.loadtxt('ss-3d.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(ss_2d[:, 0], 'r-', linewidth = 2.0)
plt.plot(ss_2d[:, 1], 'b-', linewidth = 2.0)
plt.plot(ss_3d[:, 0], 'r--', linewidth = 2.0)
plt.plot(ss_3d[:, 1], 'b--', linewidth = 2.0)
plt.xlim([0, 130])
plt.xlabel('Correlation length $r$')
plt.ylabel('Surface-surface function $F_{ss}(r)$')
plt.legend(['CorrelationFunctions.jl (2D)', 'Theory (2D)',
            'CorrelationFunctions.jl (3D)', 'Theory (3D)'])
plt.savefig('ss.png')

sv_2d = np.loadtxt('sv-2d.dat')
sv_3d = np.loadtxt('sv-3d.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(sv_2d[:, 0], 'r-', linewidth = 2.0)
plt.plot(sv_2d[:, 1], 'b-', linewidth = 2.0)
plt.plot(sv_3d[:, 0], 'r--', linewidth = 2.0)
plt.plot(sv_3d[:, 1], 'b--', linewidth = 2.0)
plt.xlim([0, 130])
plt.xlabel('Correlation length $r$')
plt.ylabel('Surface-void function $F_{sv}(r)$')
plt.legend(['CorrelationFunctions.jl (2D)', 'Theory (2D)',
            'CorrelationFunctions.jl (3D)', 'Theory (3D)'])
plt.savefig('sv.png')

ps_hist_2d = np.loadtxt('pore_size-2d-hist.dat')
ps_prob_2d = np.loadtxt('pore_size-2d-prob.dat')
ps_hist_3d = np.loadtxt('pore_size-3d-hist.dat')
ps_prob_3d = np.loadtxt('pore_size-3d-prob.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.hist(ps_hist_2d, density = True, bins = 20)
plt.hist(ps_hist_3d, density = True, bins = 20)
plt.plot(ps_prob_2d[:,0], ps_prob_2d[:,1])
plt.plot(ps_prob_3d[:,0], ps_prob_3d[:,1])
plt.xlim([0, 100])
plt.xlabel('Pore size $r$')
plt.ylabel('Pore size function $P(r)$')
plt.legend(['Theory (2D)', 'Theory (3D)',
            'CorrelationFunctions.jl (2D)', 'CorrelationFunctions.jl (3D)'])
plt.savefig('ps.png')

cl_hist_2d = np.loadtxt('chord_length-2d-hist.dat')
cl_prob_2d = np.loadtxt('chord_length-2d-prob.dat')
cl_hist_3d = np.loadtxt('chord_length-3d-hist.dat')
cl_prob_3d = np.loadtxt('chord_length-3d-prob.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.hist(cl_hist_2d, density = True, bins = 20)
plt.hist(cl_hist_3d, density = True, bins = 20)
plt.plot(cl_prob_2d[:,0], cl_prob_2d[:,1])
plt.plot(cl_prob_3d[:,0], cl_prob_3d[:,1])
plt.xlim([0, 600])
plt.xlabel('Chord length $r$')
plt.ylabel('Chord length function $p(r)$')
plt.legend(['Theory (2D)', 'Theory (3D)',
            'CorrelationFunctions.jl (2D)', 'CorrelationFunctions.jl (3D)'])
plt.savefig('cl.png')
