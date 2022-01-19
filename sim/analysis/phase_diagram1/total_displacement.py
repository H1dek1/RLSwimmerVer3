#!/usr/bin/env python3
import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

def plotTotalDisplacement(fig, ax, phase, action_intervals, max_lengths):
    ax.set_title('1 Episode displacement')
    ax.set_xlabel(r'$T^{a*}$')
    ax.set_ylabel(r'$\ell^{\rm max*}$')
    data = dict()
    for interval in action_intervals:
        for length in max_lengths:
            one_data = phase[str(round(interval, 2))][str(round(length, 2))]
            if one_data['name'] not in data:
                data[one_data['name']] = dict()
                data[one_data['name']]['x'] = list()
                data[one_data['name']]['y'] = list()
                data[one_data['name']]['displacement'] = list()
            data[one_data['name']]['x'].append(interval)
            data[one_data['name']]['y'].append(length)
            data[one_data['name']]['displacement'].append(one_data['displacement'])

    cmap_list = ['PuRd', 'GnBu']
    for idx, key in enumerate(data):
        mappable = ax.scatter(data[key]['x'], data[key]['y'], c=data[key]['displacement'], cmap=cmap_list[idx], vmin=0, vmax=3)
        fig.colorbar(mappable, ax=ax, label=f'${key}$')


def main():
    with open(
            '../data/optimals/without_energy/withoutEnergy_phaseDiagram1.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        phase = json.load(f)

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    fig, ax = plt.subplots(1, 1)
    plotTotalDisplacement(fig, ax, phase, action_intervals, max_lengths)
    plt.show()


if __name__ == '__main__':
    main()
