#!/usr/bin/env python3 
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 10

def main():
    plot_start = 1
    plot_end   = 10
    dt = 0.1

    # intervals = np.arange(0.1, 1.0, 0.2)
    # lengths = np.arange(1.1, 2.0, 0.2)
    intervals = [0.7]
    lengths = [1.9]

    for interval in tqdm(intervals):
        for length in tqdm(lengths, leave=False):
            # filename = f'../../result/radius0.1/without_energy/custom_gamma/' \
            #         f'type20_radius0.1_interval{interval:.1f}' \
            #         f'_maxlength{length:.1f}_withoutEnergy.csv'
            filename = f'../../result/' \
                    f'type20_radius0.1_interval{interval:.1f}' \
                    f'_maxlength{length:.1f}_withEnergy.csv'

            df = pd.read_csv(filename)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            #ax.set_title('StateTransition - '+type_name)
            #ax.set_aspect('equal')
            ax.set_xlabel(r'$\ell_0^*$', fontsize=20)
            ax.set_ylabel(r'$\ell_1^*$', fontsize=20)
            ax.set_zlabel(r'$\ell_2^*$', fontsize=20)
            # ax.set_xlim(1, 2)
            # ax.set_ylim(1, 2)
            # ax.set_zlim(1, 2)
            ax.view_init(elev=30, azim=10)

            ax.plot3D(df['arm_length_0'][int(plot_start/dt):int(plot_end/dt)], df['arm_length_1'][int(plot_start/dt):int(plot_end/dt)], df['arm_length_2'][int(plot_start/dt):int(plot_end/dt)], color='C0', label=filename)

            fig.savefig(f'img/custom_gamma/triangle/radius0.1/interval{interval:.1f}_length{length:.1f}.png')
            del fig
            plt.show()

if __name__ == '__main__':
    main()
