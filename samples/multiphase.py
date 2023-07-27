#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

pairs = [(1, 2), (1, 3), (2, 3)]

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 25)

for pair in pairs:
    p1, p2 = pair
    data = np.load('multiphase-%i-%i.npy' % (p1 - 1, p2 - 1))
    xs = np.arange(0, data.size) * 2.25
    plt.plot(xs, data)

plt.legend(list(map(lambda x: r'$\rho_{%i%i}$' % x, pairs)), loc = 1)
plt.xlabel('Correlation length, μm')
plt.ylabel('Cross-correlation')
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
#plt.show()
plt.savefig("multiphase-cc.png", bbox_inches = 'tight')
