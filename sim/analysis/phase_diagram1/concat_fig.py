#!/usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 10

from number_of_cycles import plotOneCyclePeriod
from one_cycle_displacement import plotOneCycleDisplacement
from total_displacement import plotTotalDisplacement

def main():
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), tight_layout=True)
    with open(
            '../data/optimals/without_energy/withoutEnergy_phaseDiagram1.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        phase = json.load(f)

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    plotOneCyclePeriod(fig, axes[0], phase, action_intervals, max_lengths)
    plotOneCycleDisplacement(fig, axes[1], phase, action_intervals, max_lengths)
    plotTotalDisplacement(fig, axes[2], phase, action_intervals, max_lengths)
    plt.show()
    fig.savefig('assembled_fig.png')


if __name__ == '__main__':
    main()
