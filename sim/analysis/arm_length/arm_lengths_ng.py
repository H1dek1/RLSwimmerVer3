#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['font.family'] = 'Times New Roman'


all_df = pd.read_csv('../../result/type10_radius0.3_period1_maxlength1.9.csv')

print(all_df.columns)

fig, ax = plt.subplots(1,1, figsize=(6, 4), tight_layout=True)
ax.set_aspect('equal')
ax.set_xlim(0.8, 2.1)
ax.set_ylim(0.8, 2.1)
ax.set_xlabel(r'$\ell_0^*$')
ax.set_ylabel(r'$\ell_1^*$')
ax.plot(all_df['arm_length_0'][:40], all_df['arm_length_1'][:40])

ax.grid()
plt.show()
fig.savefig('arm_length_ng.png')
