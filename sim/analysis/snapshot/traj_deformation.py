#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from snapshot import drawSwimmer

def main():
    df = pd.read_csv('../data/strategy_record/a_interval0.5_maxlength1.5.csv')
    fig, ax = plt.subplots(1, 2, figsize=(8,5), tight_layout=True)
    
    plot_times = [
            np.arange(3.5, 5.5+0.1, 0.5),
            np.arange(5.5, 7.5+0.1, 0.5),
            ]
    for i in range(2):
        drawSwimmer(ax[i], df, plot_times[i], ymin=0.0, ymax=0)
    arrow_dict0 = dict(arrowstyle='->', color='red', 
            connectionstyle='angle3, angleA=-95, angleB=-75', lw=2)
    ax[0].annotate('',
            xy=(0.06, -0.78),
            xytext=(-0.4, -0.75),
            arrowprops=arrow_dict0
            )
    arrow_dict1 = dict(arrowstyle='->', color='red', 
            connectionstyle='angle3, angleA=105, angleB=82', lw=2)
    ax[1].annotate('',
            xy=(-0.03, 0.70),
            xytext=(-0.5, 0.7),
            arrowprops=arrow_dict1
            )

    ax[0].set_title('(a)', loc='left', fontsize=15)
    ax[1].set_title('(b)', loc='left', fontsize=15)

    # plt.show()
    fig.savefig('alt_trajectory.pdf')


if __name__ == '__main__':
    main()
