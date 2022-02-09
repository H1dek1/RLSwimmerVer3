#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

def drawSwimmer(ax, df, plot_time, ymax=5.0, ymin=0.0):
    # ax.tick_params(labelbottom=False,
    #         labelleft=False,
    #         labelright=False,
    #         labeltop=False)
    # ax.tick_params(bottom=False,
    #         left=False,
    #         right=False,
    #         top=False)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x^*$', fontsize=25)
    ax.set_ylabel(r'$y^*$', fontsize=25)
    ax.set_xlim(-0.8, 1.0)
    ax.set_ylim(ymin-1, ymax+1)
    margin = (ymax - ymin) / (len(plot_time)-1)
    for i, t in enumerate(plot_time):
        if i == 0:
            initial = drawEachSwimmer(ax, df, t, y=ymax-margin*i, draw_center=True, alpha=(1+i)/len(plot_time))
        elif i == len(plot_time) - 1:
            final   = drawEachSwimmer(ax, df, t, y=ymax-margin*i, draw_center=True, alpha=(1+i)/len(plot_time))
        else:
            drawEachSwimmer(ax, df, t, y=ymax-margin*i, draw_center=False, alpha=(1+i)/len(plot_time))

    print('initial position:', initial)
    print('final   position:', final)
    # ax.scatter(initial[0], initial[1], color='red', marker='*')
    # ax.scatter(final[0], final[1], color='red', marker='*')
    """ extend dot line to bottom and move left to bottom of swimmer """
    # ax.vlines(x=initial[0]-np.sqrt(3)/6, ymin=final[1]-0.5, ymax=initial[1], ls='--', color='k', lw=0.5)

def drawEachSwimmer(ax, df, t, y=5.0, draw_center=False, alpha=1.0):
    dt = 0.1
    """ sphere position """
    sphere_pos = np.empty((3, 2))
    for idx in range(3):
        sphere_pos[idx] = [
                df[f'sphere_pos_{idx}_x'][int(t/dt)],
                df[f'sphere_pos_{idx}_y'][int(t/dt)] + y
                ]

    """ plot sphere """
    for idx in range(3):
        sph = patches.Circle(
                xy=sphere_pos[idx],
                radius=0.05,
                fc='k',
                zorder=1,
                alpha=alpha)
        ax.add_patch(sph)

    """ plot arms """
    ax.plot(sphere_pos.T[0], sphere_pos.T[1],c='k', lw=1, zorder=0, alpha=alpha)
    ax.plot(
            [sphere_pos[-1][0], sphere_pos[0][0]],
            [sphere_pos[-1][1], sphere_pos[0][1]],
            c='k',
            lw=1,
            zorder=0,
            alpha=alpha
            )

    if draw_center:
        return np.average(sphere_pos, axis=0)
    else:
        return
    


def main():
    strategy_type = 'a'
    df = pd.read_csv('../../result/radius0.1/without_energy/type20_radius0.1_interval0.5_maxlength1.5_withoutEnergy.csv')
    print(df.columns)
    plot_time = {'a': [], 'b': []}
    delta_t = {'a': 40, 'b': 40}
    plot_time['a'] = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    plot_time['b'] = [0.0, 0.5, 1.0, 1.5]
    for i in range(len(plot_time[strategy_type])):
        plot_time[strategy_type][i] += i * delta_t[strategy_type]

    fig, ax = plt.subplots(1, 1, figsize=(1, 6), tight_layout=True)
    drawSwimmer(ax, df, plot_time[strategy_type], ymax=18, ymin=0)
    fig.savefig('sample.png')
    plt.show()


if __name__ == '__main__':
    main()
