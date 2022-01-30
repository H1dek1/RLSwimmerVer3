#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n_sph = 3

dt = 0.1
plot_time = 20
# df = pd.read_csv('../data/strategy_record/b_interval0.5_maxlength1.5.csv')
df = pd.read_csv('../../result/radius0.1/without_energy/custom_gamma/type20_radius0.1_interval0.3_maxlength1.9_withoutEnergy.csv')

dfs = [df]
fig, ax = plt.subplots(1,1)
ax.set_xlabel('Time')
ax.set_ylabel('Displacement')

for i, df in enumerate(dfs):
    df['centroid_x'] = sum([df[f'sphere_pos_{i}_x'] for i in range(n_sph)]) / n_sph
    if i == 0:
        ax.plot(df['Time'][:int(plot_time/dt)], df['centroid_x'][:int(plot_time/dt)], lw=1.0, label='Chlamy')
    else:
        ax.plot(df['Time'][:int(plot_time/dt)], df['centroid_x'][:int(plot_time/dt)], lw=1.0, label='Figure 8')

ax.grid()
ax.legend()
plt.show()
