#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

def drawNGSwimmerTransition(ax):
    ax.axis('off')
    ax.text(-0.5, 0.2, r'$\ell_0$', ha='center', fontsize=20)
    ax.text(0.5, 0.2, r'$\ell_1$', ha='center', fontsize=20)
    ax.set_aspect('equal')
    ax.set_xlim(-2.5, 3.2)
    # ax.set_ylim(-4.0, 1.0)
    centers = 5*np.array([0.0, 0.1, 0.05, -0.06, 0.08])
    y_list = -np.linspace(0.0, 3.0, 5)
    arm_lengths = np.array([
        [1.0, 1.0],
        [1.8, 1.0],
        [1.8, 1.8],
        [1.0, 1.8],
        [1.0, 1.0],
        ])
    label_list = [
            r'$A$',
            r'$B$',
            r'$C$',
            r'$D$',
            r'$A$']
    arrow_dict = dict(arrowstyle='->', color='k', connectionstyle='angle3, angleA=-45, angleB=45', lw=2, ls='-')
    for i in range(5):
        drawOneSwimmer(ax, center=centers[i], y=y_list[i], arm_lengths=arm_lengths[i])
        ax.text(-2.2, y_list[i], label_list[i], fontsize=20, color='k', va='center', ha='center')
        if not i == 0:
            ax.annotate('',
                    xy=(2.4, y_list[i]),
                    xytext=(2.4, y_list[i-1]),
                    arrowprops=arrow_dict)
            ax.text(2.9, (y_list[i-1]+y_list[i])/2, f'{i}', fontsize=18, color='k', va='center', ha='center')
            circle = patches.Circle(xy=[2.908, (y_list[i-1]+y_list[i])/2+0.05], radius=0.2, fill=False, ec='k')
            ax.add_patch(circle)

def drawOneSwimmer(ax, center, y, arm_lengths):
    sph_pos = np.array([
        [center-arm_lengths[0], y],
        [center, y],
        [center+arm_lengths[1], y],
        ])
    ax.plot(
            [sph_pos[0][0], sph_pos[2][0]],
            [sph_pos[0][1], sph_pos[2][1]],
            color='k',
            lw=2,
            zorder=0,
            )
    for i in range(3):
        sph = patches.Circle(xy=sph_pos[i], radius=0.25, fc='lightgray', ec='k', zorder=1)
        ax.add_patch(sph)
