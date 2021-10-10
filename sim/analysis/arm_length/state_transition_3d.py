#!/usr/bin/env python3 
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 10

def main():
    plot_start = 0
    plot_end   = 100
    dt = 0.1
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.set_title('StateTransition - '+type_name)
    #ax.set_aspect('equal')
    ax.set_xlabel(r'$\ell_0^*$', fontsize=20)
    ax.set_ylabel(r'$\ell_1^*$', fontsize=20)
    ax.set_zlabel(r'$\ell_2^*$', fontsize=20)
    ax.view_init(elev=30, azim=10)

    filenames = sys.argv[1:]
    print(filenames)

    for i, filename in enumerate(filenames):
        df = pd.read_csv(filename)

        ax.plot3D(df['arm_length_0'][int(plot_start/dt):int(plot_end/dt)], df['arm_length_1'][int(plot_start/dt):int(plot_end/dt)], df['arm_length_2'][int(plot_start/dt):int(plot_end/dt)], color='C{}'.format(1-i), label=filename)

    plt.show()
    #fig.savefig('StateTransition_{}'.format(type_name))

if __name__ == '__main__':
    main()
