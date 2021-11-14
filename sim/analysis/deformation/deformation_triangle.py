#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    filename = sys.argv[1]
    df = pd.read_csv(filename)
    
    df['centroid_x'] = sum([df[f'sphere_pos_{i}_x'] for i in range(3)]) / 3
    df['centroid_y'] = sum([df[f'sphere_pos_{i}_y'] for i in range(3)]) / 3
    # df['centroid_x'] = df['sphere_pos_0_x']
    # df['centroid_y'] = df['sphere_pos_0_y']

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    #ax.set_xlim(-1, 1)
    #ax.set_ylim(-1, 1)
    ax.set_aspect('equal')

    for i in range(3):
        df[f'rel_pos_{i}_x'] = df[f'sphere_pos_{i}_x'] - df['centroid_x']
        df[f'rel_pos_{i}_y'] = df[f'sphere_pos_{i}_y'] - df['centroid_y']
        ax.plot(df[f'rel_pos_{i}_x'], df[f'rel_pos_{i}_y'], color=f'C{i}')

    plt.show()


if __name__ == '__main__':
    main()

    
