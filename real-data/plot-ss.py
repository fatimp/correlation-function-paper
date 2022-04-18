#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

names = [
    "BanderaBrown",
    "Bentheimer",
    "Berea",
    "BSG",
    "CastleGate",
    "Kirby"
]

plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 20)

for name in names:
    path = name + '_2d25um_binary.pbm-surfsurf.dat'
    data = np.loadtxt(path)
    plt.plot(np.arange(10, 500), data[10:])

plt.ticklabel_format(scilimits = (0, 0), axis = 'y')
plt.xlabel('Correlation length $r$')
plt.ylabel('$F_{ss}(r)$')
plt.legend(names)
plt.savefig('../real-data-plots/real-ss.png')
#plt.show()
