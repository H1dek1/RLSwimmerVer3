#!/usr/bin/env python3

import numpy as np
import pandas as pd
import gym
from tqdm import tqdm
import skeleton_swimmer_env

def main():
    params = {
            'swimmer_type':      203,
            'on_record':         True,
            'action_interval':   0.9,
            'max_length':        1.9,
            'consider_energy':   False,
            }
    df = pd.read_csv('sim/analysis/phase_diagram/characteristic_values/type20/displacement_energy.csv')
    ref = df[(df['action_interval'] == params['action_interval']) & (df['max_arm_length'] == params['max_length'])]
    # params['displacement_gain'] = 1.0 / ref['onestep_displacement'].values[0]
    # params['energy_gain'] = 1.0 / ref['onestep_energyconsumption'].values[0]
    params['displacement_gain'] = 1.0
    params['energy_gain'] = 1.0

    env = gym.make(
            'SkeletonSwimmer-v0',
            onRecord=params['on_record'],
            swimmer_type=params['swimmer_type'],
            action_interval=params['action_interval'],
            max_arm_length=params['max_length'],
            displacement_gain=params['displacement_gain'],
            energy_gain=params['energy_gain'],
            consider_energy=params['consider_energy'],
            )

    done = False
    rewards = []
    step_counter = 0
    print('start test')
    env.reset()
    while not done:
    # for i in tqdm(range(1)):
        print('step', step_counter)
        action = np.random.randint(-1, 2, env.action_space.shape)
        obs, reward, done, info = env.step(action)
        print('Center')
        print(info['center'])
        step_counter += 1
        rewards.append(reward)
        if done == True:
            break

    # print('final position ', info)
    # print('Episode Reward:', episode_reward)
    rewards = np.array(rewards)
    print('Min', np.min(rewards))
    print('Max', np.max(rewards))
    print('abs average', np.average(np.abs(rewards)))


if __name__ == '__main__':
    main()
