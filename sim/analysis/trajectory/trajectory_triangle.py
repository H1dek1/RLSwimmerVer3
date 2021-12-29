#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    n_sph = 3
    dt = 0.1
    plot_time = 1000
    df = pd.read_csv('../../result/type202_radius0.1_interval0.3_maxlength1.3_withoutEnergy.csv')
    # df = pd.read_csv('../../result/radius0.1/same_period_maxlength/type20_radius0.1_period0.9_maxlength1.9.csv')
    df['centroid_x'] = sum([df[f'sphere_pos_{i}_x'] for i in range(n_sph)]) / n_sph
    df['centroid_y'] = sum([df[f'sphere_pos_{i}_y'] for i in range(n_sph)]) / n_sph

    fig, ax = plt.subplots(1, 1)
    #ax.set_aspect('equal')
    #ax.set_ylim(-0.1, 0.1)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.plot(df['centroid_x'][:int(plot_time/dt)], df['centroid_y'][:int(plot_time/dt)])
    plt.show()
    fig.savefig('period0.2_length1.9.png')


if __name__ == '__main__':
    main()

