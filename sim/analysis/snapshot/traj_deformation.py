#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from snapshot import drawSwimmer

def main():
    df = pd.read_csv('../data/strategy_record/a_interval0.5_maxlength1.5.csv')
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    plot_time = np.arange(5.5, 7.5+0.1, 0.5)
    drawSwimmer(ax, df, plot_time, ymax=0.0, ymin=0.0)
    plt.show()


if __name__ == '__main__':
    main()
