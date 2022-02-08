#!/usr/bin/env python

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    n_step = {'a': 6, 'b': 3}
    strategy_name_list = ['a', 'b']
    all_strategies = dict()
    for strategy in strategy_name_list:
        with open(
                f'../data/with_energy/{strategy}_triangle.json',
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
                one_step_displacement = phases['data']['1'][str(round(interval, 2))][str(round(max_length, 2))]['displacement'] / 1000.0 * (n_step[name]*interval)
                if one_step_displacement > max_displacement:
                    max_name = name
                    max_displacement = one_step_displacement

            optimal_strategy[str(round(interval, 2))][str(round(max_length, 2))]['name'] = max_name
            optimal_strategy[str(round(interval, 2))][str(round(max_length, 2))]['displacement'] = max_displacement

    # print(optimal_strategy)
    with open('../data/optimals/with_energy/withEnergy_onecycle_displacement_1.json', mode='wt', encoding='utf-8') as f:
        json.dump(optimal_strategy, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
