#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

from ng_swimmer_transition import drawNGSwimmerTransition

def main():
    fig, ax = plt.subplots(2, 2, figsize=(10, 10), tight_layout=True)
    drawNGSwimmerTransition(ax[0][0])
    ax[0][0].set_title('(a)', loc='left')
    plt.show()


if __name__ == '__main__':
    main()
