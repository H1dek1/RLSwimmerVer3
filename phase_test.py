#!/usr/bin/env python3

import sys
from tqdm import tqdm
import numpy as np
import pandas as pd
import gym

import skeleton_swimmer_env

def main():
    swimmer_type = 20
    df = pd.DataFrame(columns=['action_interval', 'max_length', 'displacement'])
    actions = np.loadtxt(
            'swimming_method/type20/d.csv',
            delimiter=',')
    interval_list = np.round(np.arange(0.1, 1.0, 0.05), decimals=2)
    max_length_list = np.round(np.arange(1.1, 2.0, 0.05), decimals=2)
    print(interval_list)
    print(max_length_list)

    for interval in tqdm(interval_list):
        # print(f'action interval: {interval}')
        for max_length in tqdm(max_length_list, leave=False):
            env = gym.make('SkeletonSwimmer-v0', 
                    onRecord=False, 
                    swimmer_type=int(swimmer_type), 
                    action_interval=interval, 
                    max_arm_length=max_length,
                    reward_gain=1.0,
                    penalty_gain=1.0,
                    epsilon=0.0,
                    reward_per_energy=False)

            done = False
            step_counter = 0
            env.reset()
            while not done:
                action = actions[step_counter%len(actions)]
                obs, reward, done, info = env.step(action)
                step_counter += 1
                if done == True:
                    break

            df = df.append({
                'action_interval': interval,
                'max_length': max_length,
                'displacement': info['center'][0],
                }, ignore_index=True)
    df.to_csv('sim/analysis/phase_diagram/data/without_energy/d_phase.csv', index=False)


if __name__ == '__main__':
    main()
