#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def drawChlamy(ax):
    ax.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
    ax.tick_params(bottom=False,
            left=False,
            right=False,
            top=False)
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(-2.06, 2.06)
    ax.set_aspect('equal')
    e = patches.Ellipse(xy=(0, 0), width=1.0, height=0.6, fc='k', ec='k', zorder=1)
    ax.add_patch(e)
    arm0 = patches.Arc(xy=(0.4, 1.0), width=2.0, height=1.5, angle=-120, theta1=30, theta2=160, linewidth=2, color="k", zorder=0)
    arm1 = patches.Arc(xy=(0.4, -1.0), width=2.0, height=1.5, angle=-60, theta1=20, theta2=150, linewidth=2, color="k", zorder=0)
    ax.add_patch(arm0)
    ax.add_patch(arm1)

    c0 = patches.Circle(xy=(0.85, -1.2), radius=0.5, fc='w', ec='k', ls='--', fill=False, zorder=2)
    c1 = patches.Circle(xy=(0.85, 1.2), radius=0.5, fc='w', ec='k', ls='--', fill=False, zorder=2)
    ax.add_patch(c0)
    ax.add_patch(c1)


def main():
    fig, ax = plt.subplots(1, 1)
    drawChlamy(ax)
    plt.show()


if __name__ == '__main__':
    main()
