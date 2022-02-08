import numpy as np
import matplotlib.pyplot as plt

def drawStateTransition(ax):
    ax.set_aspect('equal')
    pad_x = 0.5
    pad_y = 0.5
    min_x = 0
    max_x = 1.8
    min_y = 0
    max_y = 1.0
    ax.set_xlim(min_x-pad_x, max_x+pad_x)
    ax.set_ylim(min_y-pad_y, max_y+pad_y)
    ax.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
    ax.tick_params(bottom=False,
            left=False,
            right=False,
            top=False)
    ax.axis('off')

    A = np.array([min_x, min_y])
    B = np.array([max_x, min_y])
    C = np.array([max_x, max_y])
    D = np.array([min_x, max_y])

    ax.text(A[0], A[1], 'A', fontsize=25, va='top', ha='right')
    ax.text(B[0], B[1], 'B', fontsize=25, va='top', ha='left')
    ax.text(C[0], C[1], 'C', fontsize=25, va='bottom', ha='left')
    ax.text(D[0], D[1], 'D', fontsize=25, va='bottom', ha='right')

    bbox_blue = dict(
            facecolor='white',
            edgecolor='blue',
            linewidth=1.5,
            linestyle="-")

    bbox_red = dict(
            facecolor='white',
            edgecolor='red',
            linewidth=1.5,
            linestyle="-")
    ax.text(
            (A[0]+B[0])/2,
            (A[1]+B[1])/2,
            r'$1.48 \times 10^{-2}$',
            bbox=bbox_red,
            va='center',
            ha='center',
            )
    ax.text(
            (B[0]+C[0])/2,
            (B[1]+C[1])/2,
            r'$-1.31 \times 10^{-2}$',
            bbox=bbox_blue,
            va='center',
            ha='center',
            )
    ax.text(
            (C[0]+D[0])/2,
            (C[1]+D[1])/2,
            r'$-2.25 \times 10^{-2}$',
            bbox=bbox_blue,
            va='center',
            ha='center',
            )
    ax.text(
            (D[0]+A[0])/2,
            (D[1]+A[1])/2,
            r'$2.96 \times 10^{-2}$',
            bbox=bbox_red,
            va='center',
            ha='center',
            )

    width = 0.02
    ax.quiver(
            A[0],
            A[1],
            (B[0]-A[0]),
            (B[1]-A[1]),
            color='red',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            B[0],
            B[1],
            (C[0]-B[0]),
            (C[1]-B[1]),
            color='blue',
            width=width,
            angles='xy', scale_units='xy', scale=1,
            )
    ax.quiver(
            C[0],
            C[1],
            (D[0]-C[0]),
            (D[1]-C[1]),
            color='blue',
            width=width,
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

