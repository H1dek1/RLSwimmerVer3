#!/usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 10

from displacement import plotDisplacement
from energy import plotEnergy
from efficiency import plotEfficiency
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

def main():
    # fig, axes = plt.subplots(3, 1, figsize=(6, 15), constrained_layout=True)
    fig = plt.figure(figsize=(9, 15))
    gs_master = GridSpec(nrows=3, ncols=1, height_ratios=[1, 1, 1])
    gs_master.update(top=0.97, bottom=0.05)
    gs = GridSpecFromSubplotSpec(nrows=3, ncols=1, subplot_spec=gs_master[:,:])
    axes = [
            fig.add_subplot(gs[0]),
            fig.add_subplot(gs[1]),
            fig.add_subplot(gs[2]),
            ]
    with open(
            '../data/optimals/with_energy/withEnergy_phaseDiagram_efficiency.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        efficiency_phase = json.load(f)

    with open(
            '../data/optimals/with_energy/withEnergy_phaseDiagram_displacement.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        displacement_phase = json.load(f)

    with open(
            '../data/optimals/with_energy/withEnergy_phaseDiagram_energy.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        energy_phase = json.load(f)

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    plotEfficiency(fig, axes[0], efficiency_phase,
            action_intervals, max_lengths, per_second=True, adjust_vlimit=True)
    plotDisplacement(fig, axes[1], displacement_phase,
            action_intervals, max_lengths, per_second=True, adjust_vlimit=True)
    plotEnergy(fig, axes[2], energy_phase,
            action_intervals, max_lengths, per_second=True, adjust_vlimit=True)
    axes[0].set_title('(a)', loc='left')
    axes[1].set_title('(b)', loc='left')
    axes[2].set_title('(c)', loc='left')
    # axes[0].set_aspect('equal')
    # axes[1].set_aspect('equal')
    # axes[2].set_aspect('equal')
    for ax in axes:
        ax.set_xlabel(r'$T^{a*}$')
        ax.set_ylabel(r'$\ell^{\max*}$')

    fig.canvas.draw()
    axpos0 = axes[0].get_position()
    axpos1 = axes[1].get_position()
    axpos2 = axes[2].get_position()
    # axes[0].set_position([axpos2.x0, axpos0.y0, axpos2.width, axpos0.height])
    axes[2].set_position([axpos2.x0, axpos2.y0, axpos0.width, axpos0.height])
    # plt.show()
    fig.savefig('pd_energy.pdf')


if __name__ == '__main__':
    main()
