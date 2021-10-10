#!/usr/bin/env python
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['font.family'] = 'Times New Roman'

def main():
    fake_50 = 4.0
    x = [0, 10, 30, 50, 80, 150]
    y = [0.5, 0.4, 0.3, 0.25, 0.22, 0.2]
    #coeffs = np.polyfit(x, y, 2)
    border = interpolate.interp1d(x, y, kind='cubic')
    t1 = np.arange(0, 110, 0.1)
    t2 = border(t1)


    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.set_title('Optimal Swimming Way in Velocity Based Model')
    ax.set_xlim(0.0, 4.5)
    ax.set_ylim(1.0, 2.0)
    ax.set_xticks([0.2, 1.0, fake_50])
    ax.set_xticklabels(['0.2', '1.0', '50.0'])
    ax.set_yticks([1.0, 1.1, 1.5, 1.9, 2.0])
    ax.set_xlabel(r'$T^{a*}$', fontsize=20)
    ax.set_ylabel(r'$\ell^{\rm max}$', fontsize=20)
    ax.plot([0.0, 0.1, 1.0], [1.0, 1.1, 2.0])
    # TODO Coloring
    ax.scatter(0.2, 1.1, c='C2', s=120, label='(0.2, 1.1) new typeC')
    ax.scatter(0.2, 1.5, c='C3', s=120, label='(0.2, 1.5) new typeD')
    ax.scatter(0.2, 1.9, c='C4', s=120, label='(0.2, 1.9) new typeE')
    ax.scatter(1.0, 1.1, c='C5', s=120, label='(1.0, 1.1) ???')
    ax.scatter(1.0, 1.5, c='C1', s=120, label='(1.0, 1.5) typeB')
    ax.scatter(1.0, 1.9, c='C1', s=120, label='(1.0, 1.9) typeB')
    ax.scatter(fake_50, 1.1, c='C5', s=120, label='(50, 1.1) ???')
    ax.scatter(fake_50, 1.5, c='C1', s=120, label='(50, 1.5) typeB ?')
    ax.scatter(fake_50, 1.9, c='C1', s=120, label='(50, 1.9) typeB')
    #ax.plot(t1, t2)
    #ax.fill_between(t1, t2, 1, fc='C0', alpha=0.6, zorder=0)
    #ax.fill_between(t1, 0, t2, fc='C1', alpha=0.6, zorder=0)
    ax.grid()
    ax.legend(fontsize=10)
    plt.show()


if __name__ == '__main__':
    main()
