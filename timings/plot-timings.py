#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

names2d = [
    'gpu/s2-2d.dat',
    'gpu/surfsurf-2d.dat',
    'gpu/surfvoid-2d.dat',
    'gpu/c2-2d.dat',
]

names3d = [
    'gpu/s2-3d.dat',
    'gpu/surfsurf-3d.dat',
    'gpu/surfvoid-3d.dat',
    'gpu/c2-3d.dat',
]

markers = [
    '.', 'o', 's', 'p'
]

data2d = [np.loadtxt(name) for name in names2d]
data3d = [np.loadtxt(name) for name in names3d]

labels = [
    'Two-point function',
    'Surface-surface function',
    'Surface-void function',
    'Cluster function'
]

plt.figure(dpi = 300)

for data, marker in zip(data3d, markers):
    data[:, 0] = data[:, 0] ** 3
    plt.plot(data[:, 0], data[:, 1], marker = marker)

plt.legend(labels)
plt.xlabel('Number of voxels')
plt.ylabel('Time of execution, seconds')
plt.savefig('time-3d.png')
