import numpy as np
import matplotlib.pyplot as plt

def drawArmSpaceTransition(ax):
    ax.set_xlim(0.9, 1.6)
    ax.set_ylim(0.9, 1.6)
    ax.set_zlim(0.9, 1.6)
    ax.set_xlabel(r'$\ell_0^*$', fontsize=15)
    ax.set_ylabel(r'$\ell_1^*$', fontsize=15)
    ax.set_zlabel(r'$\ell_2^*$', fontsize=15)
    ax.set_box_aspect((1,1,1))
    ax.view_init(elev=30, azim=15)

    A = np.array([1.0, 1.0, 1.0])
    B = np.array([1.5, 1.5, 1.0])
    C = np.array([1.5, 1.5, 1.5])
    D = np.array([1.0, 1.0, 1.5])
    
    ax.text(A[0], A[1]-0.15, A[2]-0.1, 'A', fontsize=20)
    ax.text(B[0], B[1]+0.05, B[2], 'B', fontsize=20)
    ax.text(C[0], C[1]+0.05, C[2], 'C', fontsize=20)
    ax.text(D[0], D[1]-0.1, D[2], 'D', fontsize=20)

    ax.quiver(
            A[0],
            A[1],
            A[2],
            (B[0]-A[0]),
            (B[1]-A[1]),
            (B[2]-A[2]),
            color='red',
            )
    ax.quiver(
            B[0],
            B[1],
            B[2],
            (C[0]-B[0]),
            (C[1]-B[1]),
            (C[2]-B[2]),
            color='blue',
            )
    ax.quiver(
            C[0],
            C[1],
            C[2],
            (D[0]-C[0]),
            (D[1]-C[1]),
            (D[2]-C[2]),
            color='blue',
            )
    ax.quiver(
            D[0],
            D[1],
            D[2],
            (A[0]-D[0]),
            (A[1]-D[1]),
            (A[2]-D[2]),
            color='red',
            )
