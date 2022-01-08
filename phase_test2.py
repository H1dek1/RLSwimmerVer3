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
    swimming_way = 'b'
    # df = pd.DataFrame(columns=['action_interval', 'max_length', 'displacement'])
    results = dict()
    results['name'] = swimming_way
    original_actions = np.loadtxt(
            f'swimming_method/type20/{swimming_way}.csv',
            delimiter=',')
    interval_list = np.round(np.arange(0.05, 1.0, 0.05), decimals=2)
    max_length_list = np.round(np.arange(1.05, 2.0, 0.05), decimals=2)
    # beat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    beat_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    print(interval_list)
    print(max_length_list)
    # exit()

    
    for beat in tqdm(beat_list):
        results[beat] = dict()
        actions = original_actions.repeat(beat, axis=0)
        for interval in tqdm(interval_list, leave=False):
            results[beat][interval] = dict()
            for max_length in tqdm(max_length_list, leave=False):
                # if beat * interval > max_length - 1:
                #     continue
                env = gym.make('SkeletonSwimmer-v0', 
                        onRecord=False, 
                        swimmer_type=int(swimmer_type), 
                        action_interval=interval, 
                        max_arm_length=max_length,
                        displacement_gain=1.0,
                        energy_gain=1.0,
                        consider_energy=False)

                done = False
                step_counter = 0
                env.reset()
                while not done:
                    action = actions[step_counter%len(actions)]
                    obs, reward, done, info = env.step(action)
                    step_counter += 1
                    if done == True:
                        break

                results[beat][interval][max_length] = info['center'][0]
                # df = df.append({
                #     'action_interval': interval,
                #     'max_length': max_length,
                #     'displacement': info['center'][0],
                #     }, ignore_index=True)
    # df.to_csv('sim/analysis/phase_diagram/data/without_energy/d_phase.csv', index=False)
    with open(f'sim/analysis/phase_diagram/data/without_energy/{swimming_way}_second.json', mode='wt', encoding='utf-8') as f:
          json.dump(results, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    main()
