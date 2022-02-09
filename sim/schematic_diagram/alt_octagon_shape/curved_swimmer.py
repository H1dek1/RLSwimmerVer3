import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

def drawCurvedSwimmer(ax):
    ax.set_xlim(-2, 6)
    ax.set_ylim(-2.0, 4.0)
    ax.set_aspect('equal')
    ax.axis('off')
    center = np.array([
        [0.0, 2.0],
        [4.0, 2.0],
        [4.0, 0.0],
        [0.0, 0.0],
        ])
    ax.quiver((center[0][0]+center[1][0])/2, (center[0][1]+center[1][1])/2, 1.0, 0.0,
            angles='xy', scale_units='xy', scale=1, pivot='middle')
    ax.quiver((center[1][0]+center[2][0])/2, (center[1][1]+center[2][1])/2, 0.0, -1.0,
            angles='xy', scale_units='xy', scale=1, pivot='middle')
    ax.quiver((center[2][0]+center[3][0])/2, (center[2][1]+center[3][1])/2, -1.0, 0.0,
            angles='xy', scale_units='xy', scale=1, pivot='middle')
    ax.quiver((center[3][0]+center[0][0])/2, (center[3][1]+center[0][1])/2, 0.0, 1.0,
            angles='xy', scale_units='xy', scale=1, pivot='middle')
    angles = np.array([
        [ np.pi/4,  np.pi/4],
        [-np.pi/4,  np.pi/4],
        [-np.pi/4, -np.pi/4],
        [-np.pi/4,  np.pi/4],
        ])
    for i in range(4):
        drawOneSwimmer(ax, center[i], angles[i], i)


def drawOneSwimmer(ax, center, angle, number):
    pos = np.array([
        [center[0]-0.5, center[1]],
        [center[0]+0.5, center[1]],
        ])
    for p in pos:
        ax.scatter(p[0], p[1], color='k', s=40)
    ax.plot(
            [pos[0][0], pos[1][0]],
            [pos[0][1], pos[1][1]],
            color='k',
            lw=2,
            )
    ax.plot(
            [pos[0][0], pos[0][0]+0.5*np.cos(np.pi-angle)[0]],
            [pos[0][1], pos[0][1]+0.5*np.sin(np.pi-angle)[0]],
            color='k',
            lw=2,
            )
    ax.plot(
            [pos[1][0], pos[1][0]+0.5*np.cos(angle)[1]],
            [pos[1][1], pos[1][1]+0.5*np.sin(angle)[1]],
            color='k',
            lw=2,
            )
    if number < 2:
        ax.text(center[0], center[1]+1.0, rf'${number+1}$', color='k', fontsize=20, va='center', ha='center')
        cir = patches.Circle(xy=(center[0], center[1]+1.0), radius=0.4, ec='k', fill=False)
        # ax.add_patch(cir)

    else:
        ax.text(center[0], center[1]-1.0, rf'${number+1}$', color='k', fontsize=20, va='center', ha='center')
        cir = patches.Circle(xy=(center[0], center[1]-1.0), radius=0.4, ec='k', fill=False)
        # ax.add_patch(cir)
