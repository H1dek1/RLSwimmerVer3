import numpy as np
import matplotlib.pyplot as plt

def drawArmSpaceTransition(ax):
    ax.set_xlim(0.9, 1.6)
    ax.set_ylim(0.9, 1.6)
    ax.set_zlim(0.9, 1.6)
    ax.set_xlabel(r'$\ell_0^*$', fontsize=20)
    ax.set_ylabel(r'$\ell_1^*$', fontsize=20)
    ax.set_zlabel(r'$\ell_2^*$', fontsize=20)
    ax.set_box_aspect((1,1,1))
    ax.view_init(elev=30, azim=35)

    A = np.array([1.0, 1.0, 1.0])
    E = np.array([1.0, 1.5, 1.0])
    D = np.array([1.0, 1.0, 1.5])
    A = np.array([1.0, 1.0, 1.0])
    G = np.array([1.5, 1.0, 1.0])
    D = np.array([1.0, 1.0, 1.5])
    A = np.array([1.0, 1.0, 1.0])
    
    ax.text(A[0], A[1]-0.05, A[2]-0.2, 'A', fontsize=25)
    ax.text(E[0], E[1]+0.03, E[2]-0.05, 'E', fontsize=25)
    ax.text(D[0], D[1]-0.05, D[2]+0.05, 'D', fontsize=25)
    ax.text(G[0]+0.2, G[1], G[2], 'G', fontsize=25)

    ax.quiver(
            A[0],
            A[1],
            A[2],
            (E[0]-A[0]),
            (E[1]-A[1]),
            (E[2]-A[2]),
            color='red',
            )
    ax.quiver(
            E[0],
            E[1],
            E[2],
            (D[0]-E[0]),
            (D[1]-E[1]),
            (D[2]-E[2]),
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
    ax.quiver(
            A[0],
            A[1],
            A[2],
            (G[0]-A[0]),
            (G[1]-A[1]),
            (G[2]-A[2]),
            color='red',
            )
    ax.quiver(
            G[0],
            G[1],
            G[2],
            (D[0]-G[0]),
            (D[1]-G[1]),
            (D[2]-G[2]),
            color='blue',
            )
