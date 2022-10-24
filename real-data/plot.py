#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys

data = sys.argv[1]
s2 = np.loadtxt(data + '-s2.dat')
l2 = np.loadtxt(data + '-l2.dat')
c2 = np.loadtxt(data + '-c2.dat')
ss = np.loadtxt(data + '-surfsurf.dat')
sv = np.loadtxt(data + '-surfvoid.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 25)
plt.plot(s2, linewidth = 2.0)
plt.plot(l2, linewidth = 2.0)
plt.plot(c2, linewidth = 2.0)
plt.plot(ss, linewidth = 2.0)
plt.plot(sv, linewidth = 2.0)
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.xlim([0, 150])
plt.xlabel('Correlation length $r$')
plt.ylabel('Correlation function')
plt.legend(['Two point function $S_2(r)$',
            'Lineal-path function $L_2(r)$',
            'Cluster function $C_2(r)$',
            'Surface-surface function $F_{ss}(r)$',
            'Surface-void function $F_{sv}(r)$'])
plt.savefig(data + '-plot.png')
