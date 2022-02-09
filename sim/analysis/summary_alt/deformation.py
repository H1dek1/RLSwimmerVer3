#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12


def drawDeformation(ax, df, draw_arms=True):
    xticks = np.arange(-1.5, 0.5, 0.5)
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.vectorize(str)(xticks))
    yticks = np.arange(-0.5, 1.0, 0.5)
    ax.set_yticks(yticks)
    ax.set_yticklabels(np.vectorize(str)(yticks))
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x^*$', fontsize=15)
    ax.set_ylabel(r'$y^*$', fontsize=15)
    
    df['centroid_x'] = sum([df[f'sphere_pos_{i}_x'] for i in range(3)]) / 3
    df['centroid_y'] = sum([df[f'sphere_pos_{i}_y'] for i in range(3)]) / 3
    if draw_arms:
        df['centroid_x'] = df['sphere_pos_0_x']
        df['centroid_y'] = df['sphere_pos_0_y']
        ax.set_xlim(-2.0, 0.5)
        ax.set_ylim(-1.5, 1.4)

    start = 0
    end = 40
    for i in range(3):
        df[f'rel_pos_{i}_x'] = df[f'sphere_pos_{i}_x'] - df['centroid_x']
        df[f'rel_pos_{i}_y'] = df[f'sphere_pos_{i}_y'] - df['centroid_y']
        ax.plot(df[f'rel_pos_{i}_x'][start:end], df[f'rel_pos_{i}_y'][start:end], color='k', ls='--')
    if draw_arms:
        sph0 = patches.Circle(
                xy=(0, 0),
                radius=0.1,
                color='k'
                )
        sph1 = patches.Circle(
                xy=(np.cos(5*np.pi/6), np.sin(5*np.pi/6)),
                radius=0.1,
                color='k'
                )
        sph2 = patches.Circle(
                xy=(np.cos(-5*np.pi/6), np.sin(-5*np.pi/6)),
                radius=0.1,
                color='k'
                )
        ax.add_patch(sph0)
        ax.add_patch(sph1)
        ax.add_patch(sph2)
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
        ax.text(-1.75,  0.55, 'E', fontsize=15, ha='left', va='bottom')
        ax.text(-1.35,  1.05, 'F', fontsize=15, ha='left', va='bottom')
        ax.text(-0.60,  0.70, 'D', fontsize=15, ha='left', va='bottom')
        ax.text(-0.80,  0.10, 'A', fontsize=15, ha='left', va='bottom')
        ax.text(-0.70, -0.65, 'A', fontsize=15, ha='left', va='bottom')
        ax.text(-1.65,  -0.95, 'G', fontsize=15, ha='left', va='bottom')
        ax.text(-1.15,  -1.50, 'H', fontsize=15, ha='left', va='bottom')
        ax.text(-0.55,  -0.95, 'D', fontsize=15, ha='left', va='bottom')
        E = np.array([-1.45, 0.68])
        F = np.array([-1.22, 1.05])
        DL = np.array([-0.85, 0.85])
        AL = np.array([-1.10, 0.50])
        left = [AL, E, F, DL, AL]

        AR = np.array([-0.95, -0.60])
        DR = np.array([-0.65, -0.90])
        H  = np.array([-1.05, -1.20])
        G  = np.array([-1.33, -0.85])
        right = [AR, G, H, DR, AR]
        for i, pos in enumerate(right):
            if i == 0: continue
            color = 'blue'
            if i == 1: color = 'red'
            if i == 4: color = 'red'
            ax.annotate('',
                    xy=(right[i][0], right[i][1]),
                    xytext=(right[i-1][0], right[i-1][1]),
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='arc3',
                        fc=color,
                        ec=color,
                        shrinkA=0.0,
                        shrinkB=0.0,
                        lw=1
                        )
                    )
        for i, pos in enumerate(left):
            if i == 0: continue
            color = 'blue'
            if i == 1: color = 'red'
            if i == 4: color = 'red'
            ax.annotate('',
                    xy=(left[i][0], left[i][1]),
                    xytext=(left[i-1][0], left[i-1][1]),
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='arc3',
                        fc=color,
                        ec=color,
                        shrinkA=0.0,
                        shrinkB=0.0,
                        lw=1
                        )
                    )



        

        """
        point0 = np.array([-1.0, 0.42])
        point1 = np.array([-1.55, 0.42])
        point2 = np.array([-1.33, 0.85])
        start = np.array([-0.42, 0.85])
        end = np.array([-0.7, 0.5])
        pointA = np.array([-1.0, 0.42])
        pointE = np.array([-1.0, 0.42])
        ax.text(-1.3, 1.0, 'F', fontsize=15, ha='left', va='bottom')

        ax.text(point1[0]-0.10, point1[1]-0.05, 'B', fontsize=15, ha='right', va='top')
        ax.text(point1[0]-0.10, -point1[1]+0.05, 'B', fontsize=15, ha='right', va='bottom')
        ax.text(point2[0]-0.05, point2[1]+0.05, 'C', fontsize=15, ha='right', va='bottom')
        ax.text(point2[0]-0.05, -point2[1]-0.05, 'C', fontsize=15, ha='right', va='top')
        ax.text(start[0]+0.05, start[1]+0.05, 'D', fontsize=15, ha='left', va='bottom')
        ax.text(start[0]+0.05, -start[1]-0.05, 'D', fontsize=15, ha='left', va='top')
        for coef in  [1, -1]:
            ax.annotate('',
                    xy=(end[0], coef*end[1]),
                    xytext=(start[0], coef*start[1]),
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='arc3',
                        fc='red',
                        ec='red',
                        shrinkA=0.0,
                        lw=1
                        )
                    )
            ax.annotate('',
                    xy=(point1[0], coef*point1[1]),
                    xytext=(point0[0], coef*point0[1]),
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='arc3',
                        fc='red',
                        ec='red',
                        shrinkB=0.0,
                        lw=1
                        )
                    )
            ax.plot(
                    np.array([point1[0], point2[0]]),
                    coef*np.array([point1[1], point2[1]]),
                    c='blue',
                    lw=1,
                    )
            ax.annotate('',
                    xy=(start[0], coef*start[1]),
                    xytext=(point2[0], coef*point2[1]),
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='arc3',
                        fc='blue',
                        ec='blue',
                        shrinkA=0.0,
                        shrinkB=0.0,
                        lw=1
                        )
                    )
        """

def main():
    filename = sys.argv[1]
    df = pd.read_csv(filename)

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    drawDeformation(ax, df, draw_arms=True)

    plt.show()


if __name__ == '__main__':
    main()

    
