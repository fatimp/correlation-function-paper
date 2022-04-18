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
    path = name + '_2d25um_binary.pbm-s2void.dat'
    data = np.loadtxt(path)
    plt.plot(data)

plt.xlabel('Correlation length $r$')
plt.ylabel('$S_2^{(void)}(r)$')
plt.legend(names)
plt.savefig('../real-data-plots/real-s2void.png')
