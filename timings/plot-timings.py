#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

names2d = [
    'chord_length-directional-2d.dat',
    'pore_size-directional-2d.dat',
    's2-directional-2d.dat',
    'l2-directional-2d.dat',
    'c2-directional-2d.dat',
    'surf2-directional-2d.dat',
    'surfvoid-directional-2d.dat',
]

names3d = [
    'chord_length-directional-3d.dat',
    'pore_size-directional-3d.dat',
    's2-directional-3d.dat',
    'l2-directional-3d.dat',
    'c2-directional-3d.dat',
    'surf2-directional-3d.dat',
    'surfvoid-directional-3d.dat',
]

markers = [
    '.', 'o', 's', 'p', '.', 'o', 's'
]

data2d = [np.loadtxt(name) for name in names2d]
data3d = [np.loadtxt(name) for name in names3d]

labels = [
    'Chord length function',
    'Pore size function',
    'Two point function',
    'Lineal-path function',
    'Cluster function',
    'Surface-surface function',
    'Surface-void function',
]

#plt.figure(dpi = 300)

for data, marker in zip(data3d, markers):
    #plt.plot(data[:, 0], data[:, 1], marker = marker)
    plt.errorbar(data[:, 0], data[:, 1], marker = marker, yerr = data[:, 2])

plt.legend(labels)
plt.xlabel('Side of an image, pixels')
plt.ylabel('Time of execution, seconds')
#plt.savefig('time-3d.png')
plt.show()
