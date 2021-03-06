#!/usr/bin/env python3

import sys
import json
from tqdm import tqdm
import numpy as np
import pandas as pd
import gym

import skeleton_swimmer_env

def main():
    swimmer_type = 20
    swimming_way = 'a_triangle'
    # df = pd.DataFrame(columns=['action_interval', 'max_length', 'displacement'])
    results = dict()
    results['name'] = swimming_way
    results['data'] = dict()
    original_actions = np.loadtxt(
            f'swimming_method/type20/{swimming_way}.csv',
            delimiter=',')
    # interval_list = np.round(np.arange(0.3, 1.0, 0.3), decimals=2)
    # max_length_list = np.round(np.arange(1.3, 2.0, 0.3), decimals=2)
    interval_list = np.round(np.arange(0.05, 1.0, 0.05), decimals=2)
    max_length_list = np.round(np.arange(1.05, 2.0, 0.05), decimals=2)
    beat_list = [1]
    # beat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    print(interval_list)
    print(max_length_list)

    
    for beat in tqdm(beat_list):
        results['data'][beat] = dict()
        actions = original_actions.repeat(beat, axis=0)
        for interval in tqdm(interval_list, leave=False):
            results['data'][beat][interval] = dict()
            for max_length in tqdm(max_length_list, leave=False):
                # if beat * interval > max_length - 1:
                #     continue
                results['data'][beat][interval][max_length] = dict()

                env = gym.make('SkeletonSwimmer-v0', 
                        onRecord=False, 
                        swimmer_type=int(swimmer_type), 
                        action_interval=interval, 
                        max_arm_length=max_length,
                        displacement_gain=1.0,
                        energy_gain=1.0,
                        consider_energy=False)

                energy_consumption = []

                done = False
                step_counter = 0
                env.reset()
                while not done:
                    action = actions[step_counter%len(actions)]
                    obs, reward, done, info = env.step(action)
                    energy_consumption.append(info['energy_consumption'].sum())
                    step_counter += 1
                    if done == True:
                        break

                results['data'][beat][interval][max_length]['displacement'] = info['center'][0]
                results['data'][beat][interval][max_length]['energy_consumption'] = np.array(energy_consumption).sum()

    # with open(f'sim/analysis/data/without_energy/{swimming_way}_v2.json', mode='wt', encoding='utf-8') as f:
    with open(f'./{swimming_way}.json', mode='wt', encoding='utf-8') as f:
          json.dump(results, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    main()
