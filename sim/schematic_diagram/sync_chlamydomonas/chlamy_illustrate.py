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
    ax.set_xlim(-3.1, 1.1)
    ax.set_ylim(-2.10, 2.10)
    ax.set_aspect('equal')
    e = patches.Ellipse(xy=(0, 0), width=1.0, height=0.6, fc='k', ec='k', zorder=1)
    ax.add_patch(e)
    arm0 = patches.Arc(xy=(-0.4, -1.0), width=2.0, height=1.5, angle=180-120, theta1=30, theta2=160, linewidth=2, color="k", zorder=0)
    arm1 = patches.Arc(xy=(-0.4, 1.0), width=2.0, height=1.5, angle=180-60, theta1=20, theta2=150, linewidth=2, color="k", zorder=0)
    ax.add_patch(arm0)
    ax.add_patch(arm1)

    c0 = patches.Circle(xy=(-0.85, -1.2), radius=0.5, fc='w', ec='k', ls='--', fill=False, zorder=2)
    c1 = patches.Circle(xy=(-0.85, 1.2), radius=0.5, fc='w', ec='k', ls='--', fill=False, zorder=2)
    ax.add_patch(c0)
    ax.add_patch(c1)

    style = "Simple,tail_width=0.5,head_width=4,head_length=8"
    kw = dict(arrowstyle=style, color='k')
    ang1 = 5*np.pi/6
    ang2 = 7*np.pi/6
    arc1 = patches.FancyArrowPatch((-0.85+0.7*np.cos(ang1+np.pi/2),-1.2+0.7*np.sin(ang1+np.pi/2)), (-0.85+0.7*np.cos(ang2+np.pi/2),-1.2+0.7*np.sin(ang2+np.pi/2)),connectionstyle=f'arc3,rad={0.3}',shrinkA=0,shrinkB=0,**kw)
    arc2 = patches.FancyArrowPatch((-0.85+0.7*np.cos(ang2-np.pi/2),1.2+0.7*np.sin(ang2-np.pi/2)), (-0.85+0.7*np.cos(ang1-np.pi/2),1.2+0.7*np.sin(ang1-np.pi/2)),connectionstyle=f'arc3,rad={-0.3}',shrinkA=0,shrinkB=0,**kw)
    ax.add_patch(arc1)
    ax.add_patch(arc2)

    ax.arrow(
            x=-1.8, y=0.0,
            dx=-1.0, dy=0,
            width=0.20,
            head_width=0.45,
            head_length=0.45,
            length_includes_head=True,
            color='red'
            )


def main():
    fig, ax = plt.subplots(1, 1)
    drawChlamy(ax)
    plt.show()


if __name__ == '__main__':
    main()
