#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

from chlamy_illustrate import drawChlamy
from model import drawTriangleSwimmer

def main():
    fig, ax = plt.subplots(1, 2, figsize=(10, 6), tight_layout=True)
    drawChlamy(ax[0])
    drawTriangleSwimmer(fig, ax[1], center=[0.0, 0.0], direction=0.0)
    ax[1].set_xlim(-1.1, 1.3)
    ax[1].set_ylim(-1.2, 1.2)
    ax[1].tick_params(
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
    fig.savefig('sync_chlamydomonas.pdf')
    plt.show()


if __name__ == '__main__':
    main()
