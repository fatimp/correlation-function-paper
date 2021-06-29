#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

names2d = [
    'l2-2d.dat', 's2-2d.dat',
    'surfsurf-2d.dat', 'surfvoid-2d.dat',
    'pore_size-2d.dat', 'chord_length-2d.dat'
]

names3d = [
    'l2-3d.dat', 's2-3d.dat',
    'surfsurf-3d.dat', 'surfvoid-3d.dat',
    'pore_size-3d.dat', 'chord_length-3d.dat'
]

markers = [
    '.', 'o', 's', 'p', '^', 'v'
]

data2d = [np.loadtxt(name) for name in names2d]
data3d = [np.loadtxt(name) for name in names3d]

labels = [
    'Lineal-path function', 'Two-point function',
    'Surface-surface function', 'Surface-void function',
    'Pore size function', 'Chord length function'
]

plt.figure(dpi = 300)

for data, marker in zip(data3d, markers):
    data[:, 0] = data[:, 0] ** 3
    plt.plot(data[:, 0], data[:, 1], marker = marker)

plt.legend(labels)
plt.xlabel('Number of voxels')
plt.ylabel('Time of execution, seconds')
plt.savefig('time-3d.png')
