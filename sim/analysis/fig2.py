#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15

from deformation.deformation_triangle import drawDeformation
from drawChlamy.chlamy_illustrate import drawChlamy

def main():
    fig, axes = plt.subplots(1, 2, figsize=(8, 6), tight_layout=True)
    df = pd.read_csv('./data/strategy_record/b_interval0.5_maxlength1.5.csv')
    drawDeformation(axes[0], df)
    axes[0].set_title('(a)', loc='left', fontsize=18)
    drawChlamy(axes[1])
    axes[1].set_title('(b)', loc='left', fontsize=18)
    fig.tight_layout()
    fig.savefig('imgs/figure_2.png')
    # plt.show()
    


if __name__ == '__main__':
    main()
