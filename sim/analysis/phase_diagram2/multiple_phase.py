#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    swimming_methods = ['a', 'd']
    dfs = []
    for method in swimming_methods:
        dfs.append(
                pd.read_csv(f'data/without_energy/{method}_phase.csv')
                )
    all_df = dfs[0][['action_interval', 'max_length']]
    for i, method in enumerate(swimming_methods):
        all_df[f'displacement_{method}'] = dfs[i]['displacement']

    print(all_df.columns)
    displacements = all_df[
            [f'displacement_{method}' for method in swimming_methods]
            ].values
    argmax_displacements = displacements.argmax(axis=1)
    all_df['max_method'] = argmax_displacements
    print(all_df)

    fig, ax = plt.subplots(1, 1)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(1.0, 2.0)
    ax.set_aspect('equal')

    for i, method in enumerate(swimming_methods):
        df_plot = all_df[all_df['max_method'] == i]
        ax.scatter(
                df_plot['action_interval'],
                df_plot['max_length'],
                c=f'C{i}',
                label=f'Method {swimming_methods[i]}'
                )

    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
