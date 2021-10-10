#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n_sph = 3

dt = 0.1
plot_time = 50
all_df = pd.read_csv('../../result/type20_radius0.3_period0.2_maxlength1.1.csv')

print(all_df.columns)

all_df['centroid_x'] = sum([all_df[f'sphere_pos_{i}_x'] for i in range(n_sph)]) / n_sph

fig, ax = plt.subplots(1,1)
ax.plot(all_df['Time'][:int(plot_time/dt)], all_df['centroid_x'][:int(plot_time/dt)], lw=1.0)
ax.grid()
plt.show()
