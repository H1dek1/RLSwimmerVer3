#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

from rl_phase_diagram.draw_rl_phase import drawRLPhase
from snapshot.snapshot import drawSwimmer

def main():
    fig = plt.figure(figsize=(8, 6), tight_layout=True)
    gs = fig.add_gridspec(1, 8)
    axes = dict()
    axes['pd'] = fig.add_subplot(gs[0, 0:6])
    axes['a'] = fig.add_subplot(gs[0, 6:7])
    axes['b'] = fig.add_subplot(gs[0, 7:8])

    """ Phase Diagram """
    drawRLPhase(fig, axes['pd'])
    axes['pd'].set_title('(a)', loc='left')

    plot_time = dict()
    """ A swimmer """
    df_a = pd.read_csv('./data/strategy_record/a_interval0.5_maxlength1.5.csv')
    plot_time['a'] = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    for i in range(len(plot_time['a'])):
        plot_time['a'][i] += i * (len(plot_time['a']) - 1) * 5

    drawSwimmer(axes['a'], df_a, plot_time['a'], ymax=18, ymin=0)
    axes['a'].set_title('(b)', loc='left')

    """ B swimmer """
    df_b = pd.read_csv('./data/strategy_record/b_interval0.5_maxlength1.5.csv')
    plot_time['b'] = [0.0, 0.5, 1.0, 1.5, 2.0]
    for i in range(len(plot_time['b'])):
        plot_time['b'][i] += i * (len(plot_time['b']) - 1) * 20

    drawSwimmer(axes['b'], df_b, plot_time['b'], ymax=18, ymin=0)
    axes['b'].set_title('(c)', loc='left')


    fig.savefig('figure_1.png')
    plt.show()




if __name__ == '__main__':
    main()
