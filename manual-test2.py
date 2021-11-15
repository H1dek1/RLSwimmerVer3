#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import gym

import skeleton_swimmer_env

def main():
    df = pd.DataFrame(columns=['trained_params', 'simulate_params', 'thousand_reward'])
    action_intervals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for idx in range(1,10):
        print(str(idx).zfill(3))
        actions = np.loadtxt(
                f'sim/optimal_action_pattern/radius0.1/' \
                f'type_20/{str(idx).zfill(3)}.csv',
                delimiter=',')

        for action_interval in action_intervals:
            is_record = False
            swimmer_type = 20
            action_period = action_interval
            max_arm_length = 1.0 + action_interval

            env = gym.make('SkeletonSwimmer-v0', 
                    isRecord=is_record, 
                    swimmer_type=int(swimmer_type), 
                    action_period=action_period, 
                    max_arm_length=max_arm_length)

            done = False
            episode_reward = 0
            step_counter = 0
            env.reset()
            while not done:
                action = actions[step_counter%len(actions)]
                #print('action:', step_counter%len(action_list))
                # print('i =', step_counter)
                # print(action)
                obs, reward, done, info = env.step(action)
                #print('reward:', reward)
                step_counter += 1
                episode_reward += reward
                if done == True:
                    break

            print('*'*20)
            print(f'idx: {idx}, action_interval: {action_interval}')
            print('final position ', info)
            print('Episode Reward:', episode_reward)
            df = df.append({
                'trained_params': idx,
                'simulate_params': 10*action_interval,
                'thousand_reward': episode_reward
                }, ignore_index=True)
    df.to_csv('sim/analysis/same_analysis/data/test_trained_result.csv', index=False)


if __name__ == '__main__':
    main()
