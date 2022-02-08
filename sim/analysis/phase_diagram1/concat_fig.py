#!/usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 10

from n_cycle import plotNumPeriod
from cycle_displacement import plotCycleDisplacement
from total_displacement import plotTotalDisplacement

def main():
    fig, axes = plt.subplots(3, 1, figsize=(6, 15), constrained_layout=True)
    with open(
            '../data/optimals/without_energy/withoutEnergy_phaseDiagram1.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        velocity_phase = json.load(f)
    with open(
            '../data/without_energy/a.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        displacement_phase = json.load(f)

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    plotNumPeriod(fig, axes[0], action_intervals, max_lengths)
    plotCycleDisplacement(fig, axes[1], displacement_phase, action_intervals, max_lengths)
    plotTotalDisplacement(fig, axes[2], velocity_phase, action_intervals, max_lengths, per_second=True)
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
    axes[0].set_position([axpos2.x0, axpos0.y0, axpos2.width, axpos0.height])
    axes[1].set_position([axpos2.x0, axpos1.y0, axpos2.width, axpos1.height])
    # plt.show()
    fig.savefig('assembled_fig.png')


if __name__ == '__main__':
    main()
