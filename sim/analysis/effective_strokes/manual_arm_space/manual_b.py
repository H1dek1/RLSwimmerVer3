#!/usr/bin/env python3 
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 10


def plotDeformationB(fig, ax, min_length=1.0, max_length=2.0):
    pos_effective = np.array([
        [min_length, min_length, max_length],
        [min_length, min_length, min_length],
            ])
    vec_effective = np.array([
        [ 0.0,  0.0, -1.0],
        [ 1.0,  1.0,  0.0],
        ])
    vec_effective *= (max_length - 1.0)

    pos_recovery = np.array([
        [max_length, max_length, min_length],
        [max_length, max_length, max_length],
            ])
    vec_recovery = np.array([
        [ 0.0,  0.0,  1.0],
        [-1.0, -1.0,  0.0],
        ])
    vec_recovery *= (max_length - 1.0)

    ax.set_xlabel(r'$\ell_0^*$', fontsize=20)
    ax.set_ylabel(r'$\ell_1^*$', fontsize=20)
    ax.set_zlabel(r'$\ell_2^*$', fontsize=20)
    ax.set_xlim(min_length, max_length)
    ax.set_ylim(min_length, max_length)
    ax.set_zlim(min_length, max_length)
    ax.view_init(elev=30, azim=20)
    ax.set_box_aspect((1,1,1))

    ax.quiver(
            pos_effective.T[0], pos_effective.T[1], pos_effective.T[2], 
            vec_effective.T[0], vec_effective.T[1], vec_effective.T[2],
            color='red',
            lw=3.0
            )
    ax.quiver(
            pos_recovery.T[0], pos_recovery.T[1], pos_recovery.T[2], 
            vec_recovery.T[0], vec_recovery.T[1], vec_recovery.T[2],
            color='blue',
            lw=3.0
            )

def main():
    max_length = 1.6
    min_length = 1.0

    fig = plt.figure(figsize=(8,8), tight_layout=True)
    ax = fig.add_subplot(111, projection='3d')
    plotDeformationB(fig, ax, min_length, max_length)

    plt.show()
    fig.savefig(f'deformation_b.png')

if __name__ == '__main__':
    main()
