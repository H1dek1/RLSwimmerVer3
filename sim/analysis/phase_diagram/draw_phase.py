#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/without_energy/a_phase.csv')
    print(df.columns)
    print('Min:', min(df['displacement']))
    print('Max:', max(df['displacement']))

    fig, ax = plt.subplots(1, 1)
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
    plt.show()


if __name__ == '__main__':
    main()
