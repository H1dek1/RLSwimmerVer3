#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15


def drawDeformation(ax, df, draw_arms=True):
    xticks = np.arange(-1.5, 0.5, 0.5)
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.vectorize(str)(xticks))
    yticks = np.arange(-0.5, 1.0, 0.5)
    ax.set_yticks(yticks)
    ax.set_yticklabels(np.vectorize(str)(yticks))
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x/\ell^{\rm min}$')
    ax.set_ylabel(r'$y/\ell^{\rm min}$')
    
    df['centroid_x'] = sum([df[f'sphere_pos_{i}_x'] for i in range(3)]) / 3
    df['centroid_y'] = sum([df[f'sphere_pos_{i}_y'] for i in range(3)]) / 3
    if draw_arms:
        df['centroid_x'] = df['sphere_pos_0_x']
        df['centroid_y'] = df['sphere_pos_0_y']
        ax.set_xlim(-1.5, 0.15)
        ax.set_ylim(-1.2, 1.1)

    end = 40
    for i in range(3):
        df[f'rel_pos_{i}_x'] = df[f'sphere_pos_{i}_x'] - df['centroid_x']
        df[f'rel_pos_{i}_y'] = df[f'sphere_pos_{i}_y'] - df['centroid_y']
        ax.plot(df[f'rel_pos_{i}_x'][:end], df[f'rel_pos_{i}_y'][:end], color='k', ls='--')
    if draw_arms:
        ax.scatter(
                [0.0, np.cos(5*np.pi/6), np.cos(-5*np.pi/6)], 
                [0.0, np.sin(5*np.pi/6), np.sin(-5*np.pi/6)], 
                color='k',
                s=300)
        ax.plot(
                [0.0, np.cos(5*np.pi/6)],
                [0.0, np.sin(5*np.pi/6)],
                color='k',
                ls='-'
                )
        ax.plot(
                [0.0, np.cos(-5*np.pi/6)],
                [0.0, np.sin(-5*np.pi/6)],
                color='k',
                ls='-'
                )
        ax.plot(
                [np.cos(5*np.pi/6), np.cos(-5*np.pi/6)],
                [np.sin(5*np.pi/6), np.sin(-5*np.pi/6)],
                color='k',
                ls='-'
                )

def main():
    filename = sys.argv[1]
    df = pd.read_csv(filename)

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    drawDeformation(ax, df, draw_arms=False)

    plt.show()


if __name__ == '__main__':
    main()

    
