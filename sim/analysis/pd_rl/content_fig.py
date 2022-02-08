#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

def main():
    fig = plt.figure(figsize=(20, 20))
    gs_master = GridSpec(
            nrows=5,
            ncols=5,
            height_ratios=[1, 1, 1, 1, 1],
            width_ratios=[1, 1, 1, 1, 1],
            )
    gs_master.update(left=0.03,right=0.99,top=0.99,bottom=0.01,wspace=0.5,hspace=0.5)
    
    gs = GridSpecFromSubplotSpec(nrows=5, ncols=5, subplot_spec=gs_master[:,:])
    ax_matrix = []
    print(gs[0, 0])
    for i in range(5):
        axes = []
        for j in range(5):
            axes.append(
                    fig.add_subplot(gs[i, j], projection='3d')
                    )
        ax_matrix.append(axes)

    action_intervals = [0.1, 0.3, 0.5, 0.7, 0.9]
    max_lengths = [1.9, 1.7, 1.5, 1.3, 1.1]
    start = 5000
    end = 10000
    for i in range(5):
        for j in range(5):
            interval = action_intervals[j]
            length = max_lengths[i]
            df = pd.read_csv(
                    '../data/without_energy/rl_phase/'
                    + 'type20_radius0.1'
                    + f'_interval{interval}_maxlength{length}'
                    + '_withoutEnergy.csv'
                    )
            ax_matrix[i][j].plot(
                    df['arm_length_0'][start:end],
                    df['arm_length_1'][start:end],
                    df['arm_length_2'][start:end],
                    )
            ax_matrix[i][j].view_init(elev=30, azim=20)
            ax_matrix[i][j].set_xlim(1, length+0.1)
            ax_matrix[i][j].set_ylim(1, length+0.1)
            ax_matrix[i][j].set_zlim(1, length+0.1)
            ax_matrix[i][j].set_xlabel(r'$\ell_0^*$', fontsize=18)
            ax_matrix[i][j].set_ylabel(r'$\ell_1^*$', fontsize=18)
            ax_matrix[i][j].set_zlabel(r'$\ell_2^*$', fontsize=18)
            ticks = np.array([1.0, 1.0+(length-1)/2, length])
            ax_matrix[i][j].set_xticks(ticks)
            ax_matrix[i][j].set_yticks(ticks)
            ax_matrix[i][j].set_zticks(ticks)
    
    # plt.show()
    fig.savefig('phase_image300.png', dpi=300)


if __name__ == '__main__':
    main()
