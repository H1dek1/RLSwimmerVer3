#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams['font.family'] = 'TImes New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

def main():
    center = np.array([-1.0, 0.0])
    direction = np.pi/8

    fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(10, 6))
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    ax.set_xlabel(r'$x$', fontsize=22)
    ax.set_ylabel(r'$y$', fontsize=22)
    xticks = np.arange(-2, 3, 1)
    yticks = np.arange(-1, 2, 1)
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.vectorize(str)(xticks), fontsize=12)
    ax.set_yticks(yticks)
    ax.set_yticklabels(np.vectorize(str)(yticks), fontsize=12)
    plotTriangleSwimmer(fig, ax, center, direction, arm_force=False)

    plt.show()
    fig.savefig('sample.pdf')

def drawTriangleSwimmer(fig, ax, center, direction, arm_force=False):
    sphere_pos, arm_vector = getEachSpherePositionAndEachArmVector(center, direction)
    drawArms(ax, sphere_pos, arm_vector)
    drawSpheres(ax, sphere_pos)
    drawArmLabel(ax, sphere_pos, direction, arm_vector)
    ax.set_aspect('equal')
    drawRadius(ax, sphere_pos)
    

def drawRadius(ax, sphere_pos):
    arrow_dict = dict(arrowstyle='<->', color='k', shrinkA=0, shrinkB=0)
    ax.annotate('', 
            xy=sphere_pos[1] - np.array([0.2, 0.0]),
            xytext=sphere_pos[1] + np.array([0.2, 0.0]),
            arrowprops=arrow_dict,
            )
    ax.text(sphere_pos[1][0]+0.3, sphere_pos[1][1]+0.2, r'$a^*$', color='k', fontsize=25)
    ax.plot(
            [sphere_pos[1][0], sphere_pos[1][0]+0.25],
            [sphere_pos[1][1], sphere_pos[1][1]+0.2],
            color='k',
            lw=0.7)
    ax.annotate('', 
            xy=sphere_pos[0] - np.array([0.5, 0.0]),
            xytext=sphere_pos[0] + np.array([0.5, 0.0]),
            arrowprops=arrow_dict,
            )
    ax.text(sphere_pos[0][0], sphere_pos[0][1]+0.15, r'$ka^*$', color='k', fontsize=25, va='center', ha='center')
    

def getEachSpherePositionAndEachArmVector(center, direction):
    dist = np.sqrt(3) / 2.0
    sphere_pos = np.empty((3, 2))
    sphere_pos[0] = center + np.array([dist*np.cos(direction+0.0), dist*np.sin(direction+0.0)])
    sphere_pos[1] = center + np.array([dist*np.cos(direction+2.0*np.pi/3.0), dist*np.sin(direction+2.0*np.pi/3.0)])
    sphere_pos[2] = center + np.array([dist*np.cos(direction-2.0*np.pi/3.0), dist*np.sin(direction-2.0*np.pi/3.0)])
    arm_vector = np.empty((3, 2))
    arm_vector[0] = sphere_pos[0] - sphere_pos[2]
    arm_vector[1] = sphere_pos[1] - sphere_pos[0]
    arm_vector[2] = sphere_pos[2] - sphere_pos[1]
    return sphere_pos, arm_vector

def drawArms(ax, sphere_pos, arm_vector):
    beam_color = 'k'
    beam_width = 8.0
    ax.plot(sphere_pos.T[0], sphere_pos.T[1], 
            c=beam_color, lw=beam_width, zorder=0)
    ax.plot(
            [sphere_pos[-1][0], sphere_pos[0][0]],
            [sphere_pos[-1][1], sphere_pos[0][1]],
            c=beam_color,
            lw=beam_width,
            zorder=0
            )
def drawSpheres(ax, sphere_pos):
    fc = 'lightgray'
    ec = 'black'
    sph_radius = 0.2
    for i, pos in enumerate(sphere_pos):
        if i == 0:
            sph = patches.Circle(xy=pos, radius=2.5*sph_radius, fc=fc, ec=ec, zorder=1)
        else:
            sph = patches.Circle(xy=pos, radius=sph_radius, fc=fc, ec=ec, zorder=1)
        ax.add_patch(sph)
        # ax.text(pos[0], pos[1], f'{i}', color='k', ha='center', va='center', fontsize=35, fontweight='normal')

def drawArmLabel(ax, sphere_pos, direction, arm_vector):
    label_size=25
    padding = 0.4
    """ arm vector """
    for i in range(3):
        text_pos = sphere_pos[i] - arm_vector[i] / 2
        text_pos += padding * np.array([arm_vector[i][1], -arm_vector[i][0]]) / np.linalg.norm(arm_vector)
        ax.text(
                text_pos[0],
                text_pos[1],
                rf'$\ell_{0}^*$',
                fontsize=label_size,
                horizontalalignment='center',
                verticalalignment='center',
                )


if __name__ == '__main__':
    main()
