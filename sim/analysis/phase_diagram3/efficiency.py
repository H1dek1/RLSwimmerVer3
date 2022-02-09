#!/usr/bin/env python3
import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

def plotEfficiency(fig, ax, phase, action_intervals, max_lengths, per_second=False, adjust_vlimit=False):
    strategy_name = {'a': 'figure eight', 'b': 'chlamy'}
    if per_second:
        # ax.set_title('velocity')
        pass
    else:
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
                data[one_data['name']]['efficiency'] = list()
            data[one_data['name']]['x'].append(interval)
            data[one_data['name']]['y'].append(length)
            data[one_data['name']]['efficiency'].append(one_data['efficiency'])

    cmap_list = ['PuRd', 'GnBu']
    if adjust_vlimit:
        vmin = min(min(data['a_triangle']['efficiency']), min(data['b_triangle']['efficiency']))
        vmax = max(max(data['a_triangle']['efficiency']), max(data['b_triangle']['efficiency']))
    else:
        vmin, vmax = None, None

    for idx, key in enumerate(data):
        print(key)
        mappable = ax.scatter(data[key]['x'], data[key]['y'], c=data[key]['efficiency'], cmap=cmap_list[idx], vmax=vmax, vmin=vmin)
        if idx == 0:
            fig.colorbar(mappable, ax=ax, label=f'Synchronous')
        else:
            fig.colorbar(mappable, ax=ax, label=f'Alternate')


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
