#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20

from snapshot import drawSwimmer 
from deformation import drawDeformation
from arm_space_transition import drawArmSpaceTransition
from state_transition import drawStateTransition

def main():
    fig = plt.figure(figsize=(14, 13))
    gs_master = GridSpec(
            nrows=2,
            ncols=3,
            height_ratios=[1, 1],
            width_ratios=[0.8, 2.0, 2.0],
            )
    gs_master.update(left=0.01,right=0.97,top=0.99,bottom=0.01,wspace=0.3,hspace=0.0)
    
    gs0 = GridSpecFromSubplotSpec(nrows=2, ncols=1, subplot_spec=gs_master[:,0])
    ax0 = fig.add_subplot(gs0[:,:])
    
    gs12 = GridSpecFromSubplotSpec(nrows=1, ncols=2, subplot_spec=gs_master[0,1:], hspace=0.0)
    ax1 = fig.add_subplot(gs12[0])
    ax2 = fig.add_subplot(gs12[1], projection='3d')
    gs3 = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[1,1:])
    ax3 = fig.add_subplot(gs3[:,:])

    df = pd.read_csv('../data/strategy_record/a_triangle_interval0.5_maxlength1.5.csv')
    """
    ax0
    """
    plot_time = {}
    plot_time['sync'] = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    for i in range(len(plot_time['sync'])):
        plot_time['sync'][i] += i * 30
    drawSwimmer(ax0, df, plot_time['sync'], ymin=0, ymax=12)
    ax0.set_title('(a)', loc='left', fontsize=25)

    """
    ax1
    """
    drawDeformation(ax1, df)
    ax1.set_title('(b)', loc='left', fontsize=25)

    """
    ax2
    """
    drawArmSpaceTransition(ax2)
    ax2.set_title('(c)', loc='left', fontsize=25)

    """
    ax3
    """
    drawStateTransition(ax3)
    ax3.set_title('(d)', loc='left', fontsize=25)

    # plt.show()
    fig.savefig('short_alt.pdf')



if __name__ == '__main__':
    main()
