#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

all_df = pd.read_csv('../../result/type10_radius0.3_period1_maxlength1.9.csv')

print(all_df.columns)

fig, ax = plt.subplots(1,1)
#ax.set_xlim(0, 9.0)
#ax.set_ylim(0.8, 2.0)
#ax.set_aspect('equal')
ax.plot(all_df['Time'][:100], all_df['arm_force_0'][:100], lw=1.0)
ax.plot(all_df['Time'][:100], all_df['arm_force_1'][:100], lw=1.0)
ax.grid()
plt.show()
