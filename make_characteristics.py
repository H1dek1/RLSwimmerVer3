#!/usr/bin/env python3
import sys
from tqdm import tqdm
import pandas as pd
import numpy as np
import gym
import skeleton_swimmer_env

action_intervals = [0.1, 0.3, 0.5, 0.7, 0.9]
max_arm_lengths  = [1.1, 1.3, 1.5, 1.7, 1.9]

df = pd.DataFrame()

for interval in action_intervals:
    for max_length in max_arm_lengths:
        env = gym.make(
                'SkeletonSwimmer-v0',
                onRecord=False,
                swimmer_type=202,
                action_interval=interval,
                max_arm_length=max_length,
                displacement_gain=1.0,
                energy_gain=1.0,
                consider_energy=False)
        env.reset()
        _, reward, done, info = env.step([0.0, 0.0, 0.0])
        
        initial_position = info['center']
        _, reward, done, info = env.step([0.0, 0.0, 1.0])
        final_position = info['center']
        
        displacement = final_position - initial_position
        print('vector', displacement)
        print('distance', np.linalg.norm(displacement))
        print('energy', sum(info['energy_penalty']))
        df = df.append({
            'action_interval': interval,
            'max_arm_length': max_length,
            'onestep_displacement': np.linalg.norm(displacement),
            'onestep_energyconsumption': sum(info['energy_penalty']),
            }, ignore_index=True)

df.to_csv('sim/analysis/phase_diagram/characteristic_values/type202/displacement_energy.csv', index=False)
