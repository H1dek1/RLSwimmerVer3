#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n_sph = 3

dt = 0.1
plot_time = 500
all_df = pd.read_csv('../../result/type20_radius0.1_period0.9_maxlength1.9.csv')
# all_df = pd.read_csv('../../result/radius0.1/same_period_maxlength/type20_radius0.1_period0.9_maxlength1.9.csv')

print(all_df.columns)

all_df['centroid_x'] = sum([all_df[f'sphere_pos_{i}_x'] for i in range(n_sph)]) / n_sph

fig, ax = plt.subplots(1,1)
ax.plot(all_df['Time'][:int(plot_time/dt)], all_df['centroid_x'][:int(plot_time/dt)], lw=1.0)
ax.grid()
plt.show()
