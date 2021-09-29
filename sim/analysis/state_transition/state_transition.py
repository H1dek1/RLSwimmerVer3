#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

all_df = pd.read_csv('result/type10_period1_maxlength1.9.csv')

print(all_df.columns)

fig, ax = plt.subplots(1,1)
ax.set_xlim(0.9, 2.0)
ax.set_ylim(0.9, 2.0)
ax.set_aspect('equal')
ax.plot(all_df['arm_length_0'], all_df['arm_length_1'], lw=0.1)
ax.grid()
plt.show()
