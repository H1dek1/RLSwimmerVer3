#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

def main():
    center = np.array([-1.0, 0.0])
    direction = 0.0

    fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(10, 7))
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel(r'$x/\ell^{\min}$', fontsize=25)
    ax.set_ylabel(r'$y/\ell^{\min}$', fontsize=25)
    xticks = np.arange(-2, 3, 1)
    yticks = np.arange(-1, 2, 1)
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.vectorize(str)(xticks), fontsize=18)
    ax.set_yticks(yticks)
    ax.set_yticklabels(np.vectorize(str)(yticks), fontsize=18)
    plotTriangleSwimmer(fig, ax, center, direction, arm_force=False)

    ax.arrow(
            x=0.8,y=0,
            dx=1.5,dy=0,
            width=0.20,
            head_width=0.45,
            head_length=0.45,
            length_includes_head=True,
            color='red')

    ax.text(
            0.8+0.75,
            0.5,
            'Target Direction',
            fontsize=25,
            horizontalalignment='center',
            verticalalignment='center',
            )
    # plt.show()
    fig.savefig('problem_statement.pdf')

def plotTriangleSwimmer(fig, ax, center, direction, arm_force=False):
    sphere_pos = getEachSpherePosition(center, direction)
    drawArms(ax, sphere_pos)
    drawSpheres(ax, sphere_pos)
    drawArmLabel(ax, sphere_pos)
    if arm_force:
        drawArmForce(ax, sphere_pos)

def getEachSpherePosition(center, direction):
    dist = np.sqrt(3) / 2.0
    sphere_pos = np.empty((3, 2))
    sphere_pos[0] = center + np.array([dist*np.cos(direction+0.0), dist*np.sin(direction+0.0)])
    sphere_pos[1] = center + np.array([dist*np.cos(direction+2.0*np.pi/3.0), dist*np.sin(direction+2.0*np.pi/3.0)])
    sphere_pos[2] = center + np.array([dist*np.cos(direction-2.0*np.pi/3.0), dist*np.sin(direction-2.0*np.pi/3.0)])
    return sphere_pos

def drawArms(ax, sphere_pos):
    beam_color = 'black'
    beam_width = 10.0
    ax.plot(sphere_pos.T[0], sphere_pos.T[1], 
            c=beam_color, lw=beam_width, zorder=0)
    ax.plot(
            [sphere_pos[-1][0], sphere_pos[0][0]],
            [sphere_pos[-1][1], sphere_pos[0][1]],
            c=beam_color,
            lw=beam_width,
            zorder=0
            )

def drawArmForce(ax, sphere_pos):
    arm_vector = np.empty((3, 2))
    arm_vector[0] = sphere_pos[0] - sphere_pos[2]
    arm_vector[1] = sphere_pos[1] - sphere_pos[0]
    arm_vector[2] = sphere_pos[2] - sphere_pos[1]
    print(sphere_pos[0][0] + 0.2*arm_vector[0][0])
    """
    arm 0
    """
    ax.arrow(
            x=sphere_pos[2][0] + 0.22*arm_vector[0][0],
            y=sphere_pos[2][1] + 0.22*arm_vector[0][1],
            dx=0.25*arm_vector[0][0],
            dy=0.25*arm_vector[0][1],
            width=0.08,
            head_width=0.20,
            head_length=0.20,
            length_includes_head=True,
            color='red',
            zorder=3)
    ax.arrow(
            x=sphere_pos[0][0] - 0.22*arm_vector[0][0],
            y=sphere_pos[0][1] - 0.22*arm_vector[0][1],
            dx=-0.25*arm_vector[0][0],
            dy=-0.25*arm_vector[0][1],
            width=0.08,
            head_width=0.20,
            head_length=0.20,
            length_includes_head=True,
            color='red',
            zorder=3)


def drawSpheres(ax, sphere_pos):
    fc = 'lightgray'
    ec = 'black'

    sph_radius = 0.3
    for pos in sphere_pos:
        sph = patches.Circle(xy=pos, radius=sph_radius, fc=fc, ec=ec, zorder=1)
        ax.add_patch(sph)

    ax.text(
            sphere_pos[0][0] + 0.7*np.cos(-np.pi/3) + 0.05,
            sphere_pos[0][1] + 0.7*np.sin(-np.pi/3) - 0.03,
            r'$S_f$',
            c='k',
            fontsize=30,
            va='center'
            )
    ax.plot(
            [sphere_pos[0][0], sphere_pos[0][0] + 0.7*np.cos(-np.pi/3)],
            [sphere_pos[0][1], sphere_pos[0][1] + 0.7*np.sin(-np.pi/3)],
            c='k',
            zorder=0
            )

    ax.text(
            sphere_pos[1][0] + 0.7*np.cos(np.pi/5) + 0.05,
            sphere_pos[1][1] + 0.7*np.sin(np.pi/5) - 0.03,
            r'$S_{b1}$',
            c='k',
            fontsize=30,
            va='center'
            )
    ax.plot(
            [sphere_pos[1][0], sphere_pos[1][0] + 0.7*np.cos(np.pi/5)],
            [sphere_pos[1][1], sphere_pos[1][1] + 0.7*np.sin(np.pi/5)],
            c='k',
            zorder=0
            )

    ax.text(
            sphere_pos[2][0] + 0.7*np.cos(-np.pi/5) + 0.05,
            sphere_pos[2][1] + 0.7*np.sin(-np.pi/5) - 0.03,
            r'$S_{b2}$',
            c='k',
            fontsize=30,
            va='center'
            )
    ax.plot(
            [sphere_pos[2][0], sphere_pos[2][0] + 0.7*np.cos(-np.pi/5)],
            [sphere_pos[2][1], sphere_pos[2][1] + 0.7*np.sin(-np.pi/5)],
            c='k',
            zorder=0
            )


def drawArmLabel(ax, sphere_pos):
    label_size=30
    ax.text(
            (sphere_pos[0][0] + sphere_pos[1][0]) / 2.0 + 0.25,
            (sphere_pos[0][1] + sphere_pos[1][1]) / 2.0 + 0.25,
            r'$\ell_1^*$',
            fontsize=label_size,
            horizontalalignment='center',
            verticalalignment='center',
            )
    ax.text(
            (sphere_pos[1][0] + sphere_pos[2][0]) / 2.0 - 0.25,
            (sphere_pos[1][1] + sphere_pos[2][1]) / 2.0 + 0.00,
            r'$\ell_2^*$',
            fontsize=label_size,
            horizontalalignment='center',
            verticalalignment='center',
            )
    ax.text(
            (sphere_pos[2][0] + sphere_pos[0][0]) / 2.0 + 0.25,
            (sphere_pos[2][1] + sphere_pos[0][1]) / 2.0 - 0.25,
            r'$\ell_0^*$',
            fontsize=label_size,
            horizontalalignment='center',
            verticalalignment='center',
            )


if __name__ == '__main__':
    main()
