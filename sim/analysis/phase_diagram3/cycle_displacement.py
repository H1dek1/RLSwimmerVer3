import numpy as np
import matplotlib.pyplot as plt

def plotCycleDisplacement(fig, ax, phase, action_intervals, max_lengths, swimming_way='a'):
    period = {'a': 8, 'b': 4}
    displacement = {
            'x': [],
            'y': [],
            'value': [],
            }
    print(phase['data']['1']['0.05']['1.05'].keys())
    phase1 = phase['data']['1']
    for interval in action_intervals:
        for length in max_lengths:
            displacement['x'].append(interval)
            displacement['y'].append(length)
            displacement['value'].append(phase1[str(np.round(interval, 4))][str(np.round(length, 4))]['displacement'] / nCycle(interval, period[swimming_way]))

    mappable = ax.scatter(
            displacement['x'],
            displacement['y'],
            c=displacement['value'],
            cmap='GnBu'
            )
    fig.colorbar(mappable, ax=ax, label='Alternate')
    

def nCycle(interval, period):
    return 1000 / (interval*period)
