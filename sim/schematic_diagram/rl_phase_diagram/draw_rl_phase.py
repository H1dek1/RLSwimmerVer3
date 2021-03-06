#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

def drawRLPhase(fig, ax):
    ax.set_xlabel(r'$T^{a*}$', fontsize=20)
    ax.set_ylabel(r'$\ell^{\rm max*}$', fontsize=20)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(1.0, 2.0)
    ax.set_aspect('equal')
    xticks = np.arange(0.1, 1.0, 0.2)
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.vectorize(str)(np.round(xticks, 2)))
    yticks = np.arange(1.1, 2.0, 0.2)
    ax.set_yticks(yticks)
    ax.set_yticklabels(np.vectorize(str)(np.round(yticks, 2)))
    
    ax.plot(
            [0.0, 1.0],
            [1.0, 2.0],
            ls='--',
            color='k',
            zorder=0,
            )

    data_list = dict()
    data_list['b'] = np.array([
        [0.1, 1.1],
        [0.3, 1.1],
        [0.5, 1.1],
        [0.7, 1.1],
        [0.9, 1.1],
        ])
    data_list['a'] = np.array([
        [0.3, 1.3],

        [0.5, 1.3],
        [0.5, 1.5],

        [0.7, 1.3],
        [0.7, 1.5],
        [0.7, 1.7],

        [0.9, 1.3],
        [0.9, 1.5],
        [0.9, 1.7],

        [0.3, 1.5],  # 
        [0.5, 1.7],  # 
        [0.7, 1.9],  # 
        [0.9, 1.9],
        ])
    data_list['c'] = np.array([
        [0.1, 1.3],
        [0.1, 1.5],
        [0.1, 1.7],
        [0.1, 1.9],
        [0.3, 1.9],
        [0.5, 1.9],
        [0.3, 1.7],
        ])
    # data_list['e'] = np.array([
    #     [0.3, 1.9],
    #     [0.5, 1.9],
    #     [0.9, 1.9],
    #         ])

    marker_list = ['s', '^', 'v', 'D']
    name = [
            'Synchronous',
            'Alternate',
            'Incomplete alternate',
            ]
    for i, data in enumerate(data_list.values()):
        ax.scatter(data.T[0], data.T[1], s=100, marker=marker_list[i], color=f'C{i}', label=name[i])

    # ax.legend(ncol=3, bbox_to_anchor=(0.78, 0.8), fontsize=13)
    ax.legend(ncol=3, loc='lower right', fontsize=13)



def main():
    fig, ax = plt.subplots(1, 1, figsize=(7, 7), tight_layout=True)
    drawRLPhase(fig, ax)
    plt.show()
    fig.savefig('rl_phase.pdf')


if __name__ == '__main__':
    main()
