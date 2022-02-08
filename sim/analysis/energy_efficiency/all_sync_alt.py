#!/usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from each_efficiency import plotSelectedData

def main():
    # fig, axes = plt.subplots(3, 1, figsize=(6, 15), constrained_layout=True)
    fig = plt.figure(figsize=(12, 15))
    gs_master = GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1], width_ratios=[1, 1])
    gs_master.update(top=0.97, bottom=0.05, left=0.1, right=0.95)
    gs = GridSpecFromSubplotSpec(nrows=3, ncols=2, subplot_spec=gs_master[:,:], hspace=0.3, wspace=0.4)
    axes = [
            fig.add_subplot(gs[0]),
            fig.add_subplot(gs[1]),
            fig.add_subplot(gs[2]),
            fig.add_subplot(gs[3]),
            fig.add_subplot(gs[4]),
            fig.add_subplot(gs[5]),
            ]
    titles = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', ]
    for ax, title in zip(axes, titles):
        ax.set_title(title, loc='left')

    file_obj_sync = open('../data/without_energy/b_v2.json', 'r')
    sync_phase = json.load(file_obj_sync)['data']['1']
    file_obj_alt = open('../data/without_energy/a_v2.json', 'r')
    alt_phase = json.load(file_obj_alt)['data']['1']

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)

    plotSelectedData(fig, axes[0], sync_phase, action_intervals, max_lengths, mode='velocity')
    plotSelectedData(fig, axes[1], alt_phase, action_intervals, max_lengths, mode='velocity')
    plotSelectedData(fig, axes[2], sync_phase, action_intervals, max_lengths, mode='energy_per_time')
    plotSelectedData(fig, axes[3], alt_phase, action_intervals, max_lengths, mode='energy_per_time')
    plotSelectedData(fig, axes[4], sync_phase, action_intervals, max_lengths, mode='efficiency')
    plotSelectedData(fig, axes[5], alt_phase, action_intervals, max_lengths, mode='efficiency')

    fig.savefig('compare_sync_alt.pdf')

if __name__ == '__main__':
    main()
