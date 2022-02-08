import numpy as np
import matplotlib.pyplot as plt

def drawStateTransition(ax):
    ax.set_aspect('equal')
    pad_x = 0.6
    pad_y = 0.3
    min_x = 0
    max_x = 2.0
    min_y = 0
    max_y = 1.2
    ax.set_xlim(-max_x-pad_x, max_x+pad_x)
    ax.set_ylim( min_y-pad_y, max_y+pad_y)
    ax.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
    ax.tick_params(bottom=False,
            left=False,
            right=False,
            top=False)
    # ax.axis('off')

    A = np.array([min_x, min_y])
    E = np.array([max_x, min_y])
    F = np.array([max_x, max_y])
    D = np.array([min_x, max_y])
    G = np.array([-max_x, min_y])
    H = np.array([-max_x, max_y])
    for pos in [A, E, F, D, G, H]:
        ax.scatter(pos[0], pos[1], s=100, color='k', zorder=5)

    ax.text(A[0], A[1]-0.1, 'A', fontsize=25, va='top', ha='center')
    ax.text(E[0], E[1]-0.1, 'E', fontsize=25, va='top', ha='left')
    ax.text(F[0], F[1]+0.1, 'F', fontsize=25, va='bottom', ha='left')
    ax.text(D[0], D[1]+0.1, 'D', fontsize=25, va='bottom', ha='center')
    ax.text(G[0], G[1]-0.1, 'G', fontsize=25, va='top', ha='right')
    ax.text(H[0], H[1]+0.1, 'H', fontsize=25, va='bottom', ha='right')

    bbox_blue = dict(
            facecolor='white',
            edgecolor='blue',
            linewidth=1.5,
            linestyle="-")
    bbox_blue_alpha = dict(
            facecolor='white',
            edgecolor='#DCDCDC',
            linewidth=1.5,
            linestyle="-")

    bbox_red = dict(
            facecolor='white',
            edgecolor='red',
            linewidth=1.5,
            linestyle="-")
    ax.text(
            (A[0]+E[0])/2,
            (A[1]+E[1])/2,
            (
                '$\\Delta x^* = 1.72 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 6.22 \\times 10^{-1}$'
                ),
            bbox=bbox_red,
            va='center',
            ha='center',
            )
    ax.text(
            (E[0]+F[0])/2,
            (E[1]+F[1])/2,
            (
                '$\\Delta x^* = -1.62 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 6.42 \\times 10^{-1}$'
                ),
            bbox=bbox_blue_alpha,
            va='center',
            ha='center',
            )
    ax.text(
            (G[0]+H[0])/2,
            (G[1]+H[1])/2,
            (
                '$\\Delta x^* = -1.52 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 6.42 \\times 10^{-1}$'
                ),
            bbox=bbox_blue_alpha,
            va='center',
            ha='center',
            )
    ax.text(
            (F[0]+D[0])/2,
            (F[1]+D[1])/2,
            (
                '$\\Delta x^* = -1.57 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 6.18 \\times 10^{-1}$'
                ),
            bbox=bbox_blue_alpha,
            va='center',
            ha='center',
            )
    ax.text(
            (H[0]+D[0])/2,
            (H[1]+D[1])/2,
            (
                '$\\Delta x^* = -1.46 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 6.18 \\times 10^{-1}$'
                ),
            bbox=bbox_blue_alpha,
            va='center',
            ha='center',
            )
    ax.text(
            (D[0]+A[0])/2,
            (D[1]+A[1])/2,
            (
                '$\\Delta x^* = 2.85 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 8.80 \\times 10^{-1}$'
                ),
            bbox=bbox_red,
            va='center',
            ha='center',
            )
    ax.text(
            (E[0]+D[0])/2,
            (E[1]+D[1])/2,
            (
                '$\\Delta x^* = -3.84 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 1.46 \\times 10^{0}$'
                ),
            bbox=bbox_blue,
            va='center',
            ha='center',
            )
    ax.text(
            (G[0]+D[0])/2,
            (G[1]+D[1])/2,
            (
                '$\\Delta x^* = -3.69 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 1.46 \\times 10^{0}$'
                ),
            bbox=bbox_blue,
            va='center',
            ha='center',
            )
    ax.text(
            (G[0]+A[0])/2,
            (G[1]+A[1])/2,
            (
                '$\\Delta x^* = 1.43 \\times 10^{-2}$\n' 
                +'$\\Delta E^* = 5.04 \\times 10^{-1}$'
                ),
            bbox=bbox_red,
            va='center',
            ha='center',
            )

    width = 0.01
    ax.quiver(
            A[0],
            A[1],
            (E[0]-A[0]),
            (E[1]-A[1]),
            color='red',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            E[0],
            E[1],
            (F[0]-E[0]),
            (F[1]-E[1]),
            color='blue',
            width=width,
            alpha=0.15,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            F[0],
            F[1],
            (D[0]-F[0]),
            (D[1]-F[1]),
            color='blue',
            width=width,
            alpha=0.15,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            D[0],
            D[1],
            (A[0]-D[0]),
            (A[1]-D[1]),
            color='red',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            A[0],
            A[1],
            (G[0]-A[0]),
            (G[1]-A[1]),
            color='red',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            G[0],
            G[1],
            (H[0]-G[0]),
            (H[1]-G[1]),
            color='blue',
            alpha=0.15,
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            H[0],
            H[1],
            (D[0]-H[0]),
            (D[1]-H[1]),
            color='blue',
            width=width,
            alpha=0.15,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            E[0],
            E[1],
            (D[0]-E[0]),
            (D[1]-E[1]),
            color='blue',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            G[0],
            G[1],
            (D[0]-G[0]),
            (D[1]-G[1]),
            color='blue',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )

