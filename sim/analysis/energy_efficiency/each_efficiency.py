#!/usr/bin/env python3 

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'TImes New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15


def main():
    strategy = 'a'
    file_object = open(f'../data/without_energy/{strategy}_v2.json', 'r')
    phase = json.load(file_object)['data']['1']
    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    fig, axes = plt.subplots(1, 3, figsize=(8, 6), tight_layout=True)
    plotSelectedData(
            fig, axes[0], phase, action_intervals, max_lengths, mode='displacement')
    plotSelectedData(
            fig, axes[1], phase, action_intervals, max_lengths, mode='energy_consumption')
    plotSelectedData(
            fig, axes[2], phase, action_intervals, max_lengths, mode='efficiency')
    plt.show()


def plotSelectedData(fig, ax, phase, action_intervals, max_lengths, mode):
    # ax.set_title(f'1 Episode {mode}')
    ax.set_xlabel(r'$T^{a*}$')
    ax.set_ylabel(r'$\ell^{\rm max*}$')

    if mode not in ['displacement', 'energy_consumption', 'efficiency', 'velocity', 'energy_per_time']:
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
            elif mode == 'velocity':
                data[mode].append(
                        phase[str(round(interval, 2))][str(round(length, 2))]['displacement'] / 1000
                        )

            elif mode == 'energy_per_time':
                data[mode].append(
                        phase[str(round(interval, 2))][str(round(length, 2))]['energy_consumption'] / 1000
                        )

            elif mode == 'efficiency':
                data[mode].append(
                        phase[str(round(interval, 3))][str(round(length, 3))]['displacement'] \
                         / phase[str(round(interval, 3))][str(round(length, 3))]['energy_consumption']
                        )
    if mode == 'efficiency':
        vmax = 0.0025
    elif mode == 'energy_per_time':
        vmax = 3
    elif mode == 'velocity':
        vmax = 0.005
    else:
        vmax=None

    cmap = 'gnuplot2'

    mappable = ax.scatter(data['interval'], data['length'], c=data[mode], vmax=vmax, cmap=cmap)
    if mode == 'efficiency':
        fig.colorbar(mappable, ax=ax, label=r'$\Delta x^* / \Delta E^*$')
    elif mode == 'velocity':
        fig.colorbar(mappable, ax=ax, label=r'$v_g$')
    elif mode == 'energy_per_time':
        fig.colorbar(mappable, ax=ax, label=r'$\Delta E^*$')

    



if __name__ == '__main__':
    main()
