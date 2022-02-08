#!/usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from efficiency_phase import plotEfficientStrategy
from velocity_phase import plotTotalDisplacement

def main():
    # fig, axes = plt.subplots(3, 1, figsize=(6, 15), constrained_layout=True)
    fig = plt.figure(figsize=(11, 16))
    gs_master = GridSpec(nrows=2, ncols=1, height_ratios=[1, 1])
    gs_master.update(top=0.97, bottom=0.05, left=0.1, right=0.95)
    gs = GridSpecFromSubplotSpec(nrows=2, ncols=1, subplot_spec=gs_master[:,:], hspace=0.3, wspace=0.4)
    axes = [
            fig.add_subplot(gs[0]),
            fig.add_subplot(gs[1]),
            ]
    action_intervals = np.round(np.arange(0.05, 1.0, 0.05), 2)
    max_lengths = np.round(np.arange(1.05, 2.0, 0.05), 2)
    axes[0].set_title('(a)', loc='left')
    axes[1].set_title('(b)', loc='left')

    with open(
            '../data/optimals/without_energy/withoutEnergy_phaseDiagram1.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        phase0 = json.load(f)
    plotTotalDisplacement(fig, axes[0], phase0, action_intervals, max_lengths, per_second=True)


    strategy_list = ['a', 'b']
    phases = dict()
    for strategy in strategy_list:
        file_object = open(f'../data/without_energy/{strategy}_v2.json', 'r')
        phases[strategy] = json.load(file_object)['data']['1']

    
    plotEfficientStrategy(fig, axes[1], phases, action_intervals, max_lengths)
    # plt.show()
    fig.savefig('two_phase.pdf')

if __name__ == '__main__':
    main()
