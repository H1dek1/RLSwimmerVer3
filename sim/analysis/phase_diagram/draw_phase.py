#!/usr/bin/env python3
import json
import numpy as np
import matplotlib.pyplot as plt

def main():
    with open(
            'optimals/withoutEnergy_phaseDiagram.json',
            mode='rt',
            encoding='utf-8'
            ) as f:
        phase = json.load(f)

    print(type(phase))
    action_intervals = np.arange(0.05, 1.0, 0.05)
    max_lengths = np.arange(1.05, 2.0, 0.05)
    optimal_strategy = []
    print(action_intervals)
    X, Y = np.meshgrid(action_intervals, max_lengths)
    
    for y in max_lengths:
        optimal_each_x = []
        for x in action_intervals:
            name = phase[str(x)][str(y)]['name']
            if name[0] == 'a':
                optimal_each_x.append(int(name[1])*x)
            elif name[0] == 'b':
                optimal_each_x.append(-int(name[1])*x)

        optimal_strategy.append(optimal_each_x)
        
    optimal_strategy = np.array(optimal_strategy)
    print(optimal_strategy)

    fig, ax = plt.subplots(1, 1)
    mappable = ax.scatter(X, Y, c=optimal_strategy, cmap='seismic', vmin=-1, vmax=1)
    fig.colorbar(mappable, ax=ax)
    plt.show()


if __name__ == '__main__':
    main()
