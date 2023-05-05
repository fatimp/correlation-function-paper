#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

names2d = [
    's2-gpu-2d.dat',
    'c2-gpu-2d.dat',
    'surf2-gpu-2d.dat',
    'surfvoid-gpu-2d.dat',
]

names3d = [
    's2-gpu-3d.dat',
    'c2-gpu-3d.dat',
    'surf2-gpu-3d.dat',
    'surfvoid-gpu-3d.dat',
]

markers = [
    '.', 'o', 's', 'p'
]

data2d = [np.loadtxt(name) for name in names2d]
data3d = [np.loadtxt(name) for name in names3d]

labels = [
    'Two point function',
    'Cluster function',
    'Surface-surface function',
    'Surface-void function',
]

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
for data, marker in zip(data3d, markers):
    plt.errorbar(data[:, 0] ** 3, data[:, 1], marker = marker, yerr = data[:, 2])
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.legend(labels)
plt.xlabel('Number of voxels')
plt.ylabel('Time of execution, seconds')
plt.savefig('time-3d-gpu.png', bbox_inches = 'tight')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
for data, marker in zip(data2d, markers):
    plt.errorbar(data[:, 0] ** 2, data[:, 1], marker = marker, yerr = data[:, 2])
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.legend(labels)
plt.xlabel('Number of pixels')
plt.ylabel('Time of execution, seconds')
plt.savefig('time-2d-gpu.png', bbox_inches = 'tight')
