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
                f'../data/without_energy/{strategy}.json',
                mode='rt',
                encoding='utf-8'
                ) as f:
            all_strategies[strategy] = json.load(f)['data']

    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    # action_intervals = np.arange(0.1, 1.0, 0.4)
    # max_lengths = np.arange(1.1, 2.0, 0.4)
    # action_intervals = np.array([0.1, 0.4, 0.7])
    # max_lengths = action_intervals + 1.0
    print(action_intervals)
    print(max_lengths)

    optimal_strategy = dict()
    for interval in action_intervals:
        """ for each interval """
        optimal_strategy[str(round(interval, 2))] = dict()
        for max_length in max_lengths:
            """ for each max length """
            optimal_strategy[str(round(interval, 2))][str(round(max_length, 2))] = dict()
            max_name = 'None'
            max_displacement = 0.0
            for name, phases in all_strategies.items():
                """ strategy A or B """
                for beat, phase in phases.items():
                    """ for each beating rhythm """
                    if phase[str(round(interval, 2))][str(round(max_length, 2))]['displacement'] > max_displacement:
                        max_name = name + beat
                        max_displacement = phase[str(round(interval, 2))][str(round(max_length, 2))]['displacement']

            # print(max_name)
            if round(interval, 2) == 0.95 and round(max_length, 2) == 1.05:
                print(max_name, max_displacement)
            optimal_strategy[str(round(interval, 2))][str(round(max_length, 2))]['name'] = max_name
            optimal_strategy[str(round(interval, 2))][str(round(max_length, 2))]['displacement'] = max_displacement

    # print(optimal_strategy)
<<<<<<< HEAD
    with open('../data/optimals/withoutEnergy_phaseDiagram2.json', mode='wt', encoding='utf-8') as f:
=======
    with open('../data/optimals/without_energy/withoutEnergy_phaseDiagram2.json', mode='wt', encoding='utf-8') as f:
>>>>>>> 901802ed8d6dee0f63b7156344e6531592b2d2d0
        json.dump(optimal_strategy, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
