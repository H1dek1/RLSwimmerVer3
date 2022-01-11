#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n_sph = 3

dt = 0.1
plot_time = 20
df1 = pd.read_csv('../../result/type20_radius0.1_interval0.3_maxlength1.7_withoutEnergy.csv')

dfs = [df1]
fig, ax = plt.subplots(1,1)

for df in dfs:
    df['centroid_x'] = sum([df[f'sphere_pos_{i}_x'] for i in range(n_sph)]) / n_sph
    ax.plot(df['Time'][:int(plot_time/dt)], df['centroid_x'][:int(plot_time/dt)], lw=1.0)

ax.grid()
plt.show()
