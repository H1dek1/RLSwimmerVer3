#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    dt = 0.1
    max_time = 1
    max_step = int(max_time / dt)
    df = pd.read_csv('../../result/type20_radius0.1_interval0.3_maxlength1.3_epsilon0.csv')
    print(df.columns)

    fig, axes = plt.subplots(2, 1)
    axes[0].plot(df['Time'][:max_step], df['arm_energy_consumption_0'][:max_step])
    axes[0].plot(df['Time'][:max_step], df['arm_energy_consumption_1'][:max_step])
    axes[0].plot(df['Time'][:max_step], df['arm_energy_consumption_2'][:max_step])
    axes[1].plot(df['Time'][:max_step], df['arm_force_0'][:max_step])
    axes[1].plot(df['Time'][:max_step], df['arm_force_1'][:max_step])
    axes[1].plot(df['Time'][:max_step], df['arm_force_2'][:max_step])
    plt.show()


if __name__ == '__main__':
    main()
