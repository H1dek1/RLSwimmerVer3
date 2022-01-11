#!/usr/bin/env python3 

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'TImes New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12


def main():
    strategy = 'b'
    file_object = open(f'../data/without_energy/{strategy}_v2.json', 'r')
    phase = json.load(file_object)['data']['1']
    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    fig, axes = plt.subplots(1, 3, figsize=(10, 3), tight_layout=True)
    plotDisplacementPerEpisode(
            fig, axes[0], phase, action_intervals, max_lengths, mode='displacement')
    plotDisplacementPerEpisode(
            fig, axes[1], phase, action_intervals, max_lengths, mode='energy_consumption')
    plotDisplacementPerEpisode(
            fig, axes[2], phase, action_intervals, max_lengths, mode='efficiency')
    plt.show()
    fig.savefig(f'efficiency_{strategy}.png')


def plotDisplacementPerEpisode(fig, ax, phase, action_intervals, max_lengths, mode):
    ax.set_title(f'1 Episode {mode}')
    ax.set_xlabel(r'$T^{a*}$')
    ax.set_ylabel(r'$\ell^{\rm max*}$')

    if mode not in ['displacement', 'energy_consumption', 'efficiency']:
        return

    data = {
            'interval': [],
            'length': [],
            mode: [],
            }
    for interval in action_intervals:
        for length in max_lengths:
            data['interval'].append(interval)
            data['length'].append(length)
            if mode == 'displacement' or mode == 'energy_consumption':
                data[mode].append(
                        phase[str(round(interval, 2))][str(round(length, 2))][mode]
                        )
            elif mode == 'efficiency':
                data[mode].append(
                        phase[str(round(interval, 3))][str(round(length, 3))]['displacement'] \
                         / phase[str(round(interval, 3))][str(round(length, 3))]['energy_consumption']
                        )
    if mode == 'efficiency':
        vmax = 6.0
    else:
        vmax=None

    cmap = 'gnuplot2'

    mappable = ax.scatter(data['interval'], data['length'], c=data[mode], vmax=vmax, cmap=cmap)
    fig.colorbar(mappable, ax=ax, label=mode)

    



if __name__ == '__main__':
    main()
