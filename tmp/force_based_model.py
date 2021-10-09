#!/usr/bin/env python
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['font.family'] = 'Times New Roman'

def main():
    x = [0, 10, 30, 50, 80, 150]
    y = [0.5, 0.4, 0.3, 0.25, 0.22, 0.2]
    #coeffs = np.polyfit(x, y, 2)
    border = interpolate.interp1d(x, y, kind='cubic')
    t1 = np.arange(0, 110, 0.1)
    t2 = border(t1)


    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.set_title('Optimal Swimming Way in Force Based Model')
    ax.set_xlim(0.0, 105)
    ax.set_ylim(0.0, 0.35)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ax.set_yticks([0.1, 0.2, 0.3])
    ax.set_xlabel(r'$T^{a*}$', fontsize=20)
    ax.set_ylabel(r'$\alpha$', fontsize=20)
    ax.plot(t1, t2)
    #ax.scatter(
    #        [30, 100],
    #        [0.3, 0.2],
    #        color='k',
    #        #s=10
    #        zorder=1
    #        )
    ax.fill_between(t1, t2, 1, fc='C0', alpha=0.6, zorder=0)
    ax.fill_between(t1, 0, t2, fc='C1', alpha=0.6, zorder=0)
    ax.grid()
    plt.show()


if __name__ == '__main__':
    main()
