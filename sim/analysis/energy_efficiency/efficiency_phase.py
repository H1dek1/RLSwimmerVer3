#!/usr/bin/env python3 

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'TImes New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15


def main():
    strategy_list = ['b', 'a']
    phase = dict()
    for strategy in strategy_list:
        file_object = open(f'../data/without_energy/{strategy}_v2.json', 'r')
        # file_object = open(f'../../../{strategy}_v2.json', 'r')
        phase[strategy] = json.load(file_object)['data']['1']

    action_intervals = np.round(np.arange(0.05, 1.0, 0.05), 2)
    max_lengths = np.round(np.arange(1.05, 2.0, 0.05), 2)
    print(action_intervals)

    fig, ax = plt.subplots(1, 1, figsize=(15, 6), tight_layout=True)
    plotEfficientStrategy(
            fig, ax, phase, action_intervals, max_lengths)
    plt.show()


def plotEfficientStrategy(fig, ax, phases, action_intervals, max_lengths):
    # ax.set_title(f'1 Efficient Phase')
    ax.set_xlabel(r'$T^{a*}$', fontsize=20)
    ax.set_ylabel(r'$\ell^{\rm max*}$', fontsize=20)

    data = dict()
    for name in phases:
        data[name] = {
                'interval': [],
                'length': [],
                'efficiency': []
                }

    for interval in action_intervals:
        for length in max_lengths:
            max_name = None
            max_efficiency = 0
            for name, phase in phases.items():
                efficiency = phase[str(interval)][str(length)]['displacement'] / phase[str(interval)][str(length)]['energy_consumption']
                if efficiency > max_efficiency:
                    max_name = name
                    max_efficiency = efficiency

            data[max_name]['interval'].append(interval)
            data[max_name]['length'].append(length)
            data[max_name]['efficiency'].append(max_efficiency)
                
    # cmap_list = ['PuRd', 'GnBu']
    # for name, each_data in data.items():
    #     mappable = ax.scatter(each_data['interval'], each_data['length'], c=each_data['efficiency'], cmap=cmap_list.pop(), vmax=None)
    #     if name == 'a':
    #         fig.colorbar(mappable, ax=ax, label='Alternate')
    #     elif name == 'b':
    #         fig.colorbar(mappable, ax=ax, label='Synchronous')
    mappableB = ax.scatter(data['b']['interval'], data['b']['length'], c=data['b']['efficiency'], cmap='PuRd', vmax=None)
    fig.colorbar(mappableB, ax=ax, label='Synchronous')
    mappableA = ax.scatter(data['a']['interval'], data['a']['length'], c=data['a']['efficiency'], cmap='GnBu', vmax=None)
    fig.colorbar(mappableA, ax=ax, label='Alternate')

    # cmap = 'gnuplot2'

    # mappable = ax.scatter(data['interval'], data['length'], c=data[mode], vmax=vmax, cmap=cmap)
    # fig.colorbar(mappable, ax=ax, label=mode)

    



if __name__ == '__main__':
    main()
