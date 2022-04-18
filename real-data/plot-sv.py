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
    path = name + '_2d25um_binary.pbm-surfvoid.dat'
    data = np.loadtxt(path)
    plt.plot(data)

plt.ticklabel_format(scilimits = (0, 0), axis = 'y')
plt.xlabel('Correlation length $r$')
plt.ylabel('$F_{sv}(r)$')
plt.legend(names)
plt.savefig('../real-data-plots/real-sv.png')
#plt.show()
