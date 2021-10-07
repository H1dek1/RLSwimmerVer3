#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['font.family'] = 'Times New Roman'


all_df = pd.read_csv('../../result/type10_radius0.3_period1_maxlength1.9.csv')

print(all_df.columns)

fig, axes = plt.subplots(2,2, figsize=(12, 12), tight_layout=True)
axes[0][0].set_title('Arm Length Space')
axes[0][0].set_aspect('equal')
axes[0][0].set_xlim(0.8, 2.1)
axes[0][0].set_ylim(0.8, 2.1)
axes[0][0].set_xlabel(r'$\ell_0^*$')
axes[0][0].set_ylabel(r'$\ell_1^*$')
axes[0][1].set_title('Arm Force Space')
axes[0][1].set_aspect('equal')
axes[0][1].set_xlim(-6.5, 6.5)
axes[0][1].set_ylim(-6.5, 6.5)
axes[0][1].set_xlabel(r'$A_0^*$')
axes[0][1].set_ylabel(r'$A_1^*$')
#axes[1][0].set_xlim(0.8, 2.1)
#axes[1][0].set_ylim(0.8, 2.1)
axes[1][0].set_xlabel('time')
axes[1][0].set_ylabel('Arm Length')
axes[1][1].set_xlabel('time')
axes[1][1].set_ylabel('Arm Force')

plot_length = 40
axes[1][1].plot(all_df['Time'][:plot_length], all_df['arm_force_0'][:plot_length], c='k', zorder=0)
axes[1][1].plot(all_df['Time'][:plot_length], all_df['arm_force_1'][:plot_length], c='k', zorder=0, ls='--')
for i in range(plot_length):
    #if i % 2 != 0: continue
    axes[0][0].scatter(all_df['arm_length_0'][i], all_df['arm_length_1'][i], c=i, cmap='cool', vmin=0, vmax=plot_length)
    axes[0][1].scatter(all_df['arm_force_0'][i], all_df['arm_force_1'][i], c=i, cmap='cool', vmin=0, vmax=plot_length)
    if i == plot_length - 1:
        axes[1][0].scatter(all_df['Time'][i], all_df['arm_length_0'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, label=r'$\ell_0^*$', marker='^')
        axes[1][0].scatter(all_df['Time'][i], all_df['arm_length_1'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, label=r'$\ell_1^*$', marker='o')
        axes[1][1].scatter(all_df['Time'][i], all_df['arm_force_0'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, label=r'$A_0^*$', marker='^')
        axes[1][1].scatter(all_df['Time'][i], all_df['arm_force_1'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, label=r'$A_1^*$', marker='o')

    axes[1][0].scatter(all_df['Time'][i], all_df['arm_length_0'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, marker='^')
    axes[1][0].scatter(all_df['Time'][i], all_df['arm_length_1'][i], c=i, cmap='cool', vmin=0, vmax=plot_length)
    axes[1][1].scatter(all_df['Time'][i], all_df['arm_force_0'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, marker='^')
    axes[1][1].scatter(all_df['Time'][i], all_df['arm_force_1'][i], c=i, cmap='cool', vmin=0, vmax=plot_length, marker='o')


axes[0][0].grid()
axes[0][1].grid()
axes[1][0].grid()
axes[1][1].grid()
axes[1][0].legend()
axes[1][1].legend()
plt.show()
fig.savefig('arm_length_force_ng.png')
