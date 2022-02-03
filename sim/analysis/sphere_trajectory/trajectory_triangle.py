#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    start = 0
    end = 5000

    # df = pd.read_csv('../data/strategy_record/b_interval0.5_maxlength1.5.csv')
    df = pd.read_csv('../../result/radius0.1/without_energy/same_gamma/type20_radius0.1_interval0.9_maxlength1.9_withoutEnergy.csv')

    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    #ax.set_ylim(-0.1, 0.1)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')

    for i in range(3):
        ax.plot(
                df[f'sphere_pos_{i}_x'][start:end],
                df[f'sphere_pos_{i}_y'][start:end],
                )
    plt.show()
    # fig.savefig('period0.2_length1.9.png')


if __name__ == '__main__':
    main()

