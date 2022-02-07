#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

from border_k import drawK
from model import drawTriangleSwimmer

def main():
    fig, ax = plt.subplots(1, 2, figsize=(10, 5), constrained_layout=False)
    fig.subplots_adjust(wspace=0.3, left=0.02, right=0.98)
    drawTriangleSwimmer(fig, ax[0], center=[0.0, 0.0], direction=0.0)
    ax[0].set_xlim(-1.1, 1.5)
    ax[0].set_ylim(-1.2, 1.2)
    ax[0].tick_params(
            bottom=False,
            left=False,
            right=False,
            top=False,
            labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
    ax[0].set_title('(a)', loc='left', fontsize=20)
    ax[1].set_title('(b)', loc='left', fontsize=20)

    drawK(ax[1])
    ax[1].text(1.02, -0.02, r'$k_c$', ha='center', va='center', fontsize=30)
    
    ax0_pos = ax[0].get_position()
    ax1_pos = ax[1].get_position()
    ax[1].set_position([ax1_pos.x0, ax1_pos.y0, ax0_pos.width, ax0_pos.height])

    plt.show()
    fig.savefig('top_heavy.pdf')


if __name__ == '__main__':
    main()
