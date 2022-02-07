import numpy as np
import matplotlib.pyplot as plt

def plotNumPeriod(fig, ax, action_intervals, max_lengths, swimming_way='b'):
    period = {'a': 8, 'b': 4}
    X, Y = np.meshgrid(action_intervals, max_lengths)
    Z = calcNumPeriod(X, Y, period[swimming_way])
    mappable = ax.scatter(X, Y, c=Z, cmap='PuRd', vmin=0, vmax=5)
    fig.colorbar(mappable, ax=ax, label='Synchronous')



def calcNumPeriod(interval, length, period):
    return 1.0 / (period*interval)

