#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 18

def main():
    img = plt.imread('phase_image300.png')
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 10), tight_layout=True)
    ax.imshow(img)
    ax.set_aspect('equal')
    xticks = [200, 600, 1000, 1400, 1800,]
    xticks = [3 * x for x in xticks]
    xticklabels = [r'$0.1$', r'$0.3$', r'$0.5$', r'$0.7$', r'$0.9$', ]
    yticks = [3*2000 - x for x in xticks]
    yticklabels = [r'$1.1$', r'$1.3$', r'$1.5$', r'$1.7$', r'$1.9$', ]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    ax.set_xlabel(r'$T^{a*}$', fontsize=20)
    ax.set_ylabel(r'$\ell^{\max*}$', fontsize=20)

    # plt.show()
    fig.savefig('pd_rl_noenergy.pdf')



if __name__ == '__main__':
    main()
