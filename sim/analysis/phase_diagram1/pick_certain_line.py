#!/usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15


def main():
    strategy_name_list = ['a', 'b']
    all_strategies = dict()
    for strategy_name in strategy_name_list:
        with open(
                f'data/without_energy/{strategy_name}_editted.json',
                mode='rt',
                encoding='utf-8'
                ) as f:
            all_strategies[strategy_name] = json.load(f)['data']['1']

    action_interval = str(0.6)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    print(all_strategies.keys())
    displacement = dict()
    for strategy_name in strategy_name_list:
        displacement[strategy_name] = []
        for length in max_lengths:
            displacement[strategy_name].append(
                    # all_strategies[strategy_name][action_interval][str(round(length, 2))]
                    all_strategies[strategy_name][str(round(length-1, 2))][str(round(length, 2))]
                    )

    fig, ax = plt.subplots(1, 1, figsize=(8, 3), tight_layout=True)
    # ax.set_title(r'$T^{a*}' + rf'={action_interval}$')
    ax.set_xlabel(r'$\ell^{\rm max*}$')
    for strategy_name in strategy_name_list:
        ax.plot(max_lengths, displacement[strategy_name])
    plt.show()
    # fig.savefig(f't{action_interval}.png')
    fig.savefig(f'same.png')


if __name__ == '__main__':
    main()
