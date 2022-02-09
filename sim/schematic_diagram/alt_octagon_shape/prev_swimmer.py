#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

from ng_swimmer_transition import drawNGSwimmerTransition
from pushmepullyou import drawPushMePullYou
from alt_octa import armSpaceSetting, drawSquare
from curved_swimmer import drawCurvedSwimmer

def main():
    fig = plt.figure(figsize=(10, 8))
    gsMaster = GridSpec(
            nrows=2,
            ncols=2,
            height_ratios=[1, 1],
            width_ratios=[1, 1],
            )
    gsMaster.update(left=0.04, right=0.98, bottom=0.08, top=0.98, wspace=0.0, hspace=0.2)
    gsUpper = GridSpecFromSubplotSpec(nrows=1, ncols=2, subplot_spec=gsMaster[0,:], wspace=0.6)
    ax0 = fig.add_subplot(gsUpper[0])
    ax1 = fig.add_subplot(gsUpper[1])
    drawCurvedSwimmer(ax0)
    drawPushMePullYou(ax1)
    ax0.set_title('(a)', loc='left', fontsize=20)
    ax1.set_title('(b)', loc='left', pad=15, fontsize=20)

    gsLower = GridSpecFromSubplotSpec(nrows=1, ncols=2, subplot_spec=gsMaster[1,:], wspace=0.0)
    ax2 = fig.add_subplot(gsLower[0])
    ax3 = fig.add_subplot(gsLower[1])
    ax2.set_title('(c)', loc='left', pad=50, fontsize=20)
    ax3.set_xlim(0.8, 1.5)
    ax3.set_ylim(0.8, 1.5)
    ax3.set_aspect('equal')
    ax3.tick_params(bottom=False,
            left=False,
            right=False,
            top=False)

    drawSquare(ax3)
    drawNGSwimmerTransition(ax2)
    plt.show()
    fig.savefig('prev_swimmer.pdf')



if __name__ == '__main__':
    main()
