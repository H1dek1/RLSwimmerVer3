#!/usr/bin/env python

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    strategy_name_list = ['a', 'b']
    all_strategies = dict()
    for strategy in strategy_name_list:
        with open(
                f'data/without_energy/{strategy}.json',
                mode='rt',
                encoding='utf-8'
                ) as f:
            all_strategies[strategy] = json.load(f)

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    # action_intervals = np.arange(0.1, 1.0, 0.4)
    # max_lengths = np.arange(1.1, 2.0, 0.4)
    # action_intervals = np.array([0.1, 0.4, 0.7])
    # max_lengths = action_intervals + 1.0
    print(action_intervals)

    optimal_strategy = dict()
    for interval in action_intervals:
        """ for each interval """
        optimal_strategy[interval] = dict()
        for max_length in max_lengths:
            """ for each max length """
            optimal_strategy[interval][max_length] = dict()
            max_name = 'None'
            max_displacement = 0.0
            for name, phases in all_strategies.items():
                """ strategy A or B """
                if 'name' in phases:
                    phases.pop('name')
                for beat, phase in phases.items():
                    """ for each beating rhythm """
                    if phase[str(round(interval, 2))][str(round(max_length, 2))] > max_displacement:
                        max_name = name + beat
                        max_displacement = phase[str(round(interval, 2))][str(round(max_length, 2))]

            # print(max_name)
            optimal_strategy[interval][max_length]['name'] = max_name
            optimal_strategy[interval][max_length]['displacement'] = max_displacement

    # print(optimal_strategy)
    with open('optimals/withoutEnergy_phaseDiagram.json', mode='wt', encoding='utf-8') as f:
        json.dump(optimal_strategy, f, ensure_ascii=False, indent=2)
                    



    exit()
    df = pd.read_csv('data/without_energy/a_phase.csv')
    print(df.columns)
    print('Min:', min(df['displacement']))
    print('Max:', max(df['displacement']))

    fig, ax = plt.subplots(1, 1)
    ax.set_xlabel('action interval')
    ax.set_ylabel('max length')
    ax.set_xlim(0, 1.0)
    ax.set_ylim(1.0, 2.0)
    ax.set_aspect('equal')
    color_bar = ax.scatter(
            df['action_interval'],
            df['max_length'],
            c=df['displacement'],
            cmap='viridis',
            vmin=0.0,
            vmax=5.1,
            )
    fig.colorbar(color_bar)
    fig.savefig('a_phase.png')
    plt.show()


if __name__ == '__main__':
    main()
