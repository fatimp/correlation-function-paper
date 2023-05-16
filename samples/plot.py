#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = [
    "Bentheimer_2d25um_binary",
    "CastleGate_2d25um_binary",
    "Kirby_2d25um_binary"
]

def load_data(name, fn):
    return np.load("%s-%s.npy" % (name, fn))

def plot_fn(fn, ylabel, power):
    plt.figure(figsize = (10, 8), dpi = 300)
    plt.rc('font', size = 18)

    for n in data:
        d = load_data(n, fn) * (1/2.25)**power
        xs = np.arange(0, d.size) * 2.25
        plt.plot(xs, d)

    plt.legend(list(map(lambda name: name.split('_')[0], data)))
    plt.xlabel('Correlation length, μm')
    plt.ylabel(ylabel)
    plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
    plt.savefig("%s-xct.png" % fn, bbox_inches = 'tight')

plot_fn('s2', '$S_2$', 0)
plot_fn('l2', '$L_2$', 0)
plot_fn('c2', '$C_2$', 0)
plot_fn('surf2', '$F_{ss}, \mu m^{-2}$', 2)
plot_fn('surfvoid', '$F_{sv}, \mu m^{-1}$', 1)
