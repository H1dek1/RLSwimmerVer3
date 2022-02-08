#!/usr/bin/env python3

import numpy as np
import pandas as pd
import gym
import skeleton_swimmer_env

def main():
    original_actions = np.loadtxt('swimming_method/type20/b.csv', delimiter=',')
    actions = original_actions.repeat(1, axis=0)
    params = {
            'swimmer_type':       20,
            'on_record':          False,
            'action_interval':    0.5,
            'max_length':         1.5,
            'consider_energy':    True,
            'random_init_states': False
            }
    df = pd.read_csv('sim/analysis/data/characteristic_values/type202/displacement_energy.csv')
    ref = df[(df['action_interval'] == params['action_interval']) & (df['max_arm_length'] == params['max_length'])]
    params['displacement_gain'] = 1.0 / ref['onestep_displacement'].values[0]
    params['energy_gain'] = 1.0 / ref['onestep_energyconsumption'].values[0]
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
            random_init_states=params['random_init_states']
            )

    """
    actions = np.array([
        [1, 1, -1],
        [-0.5, 1, -1],
        [-1, 1, 1],
        [-1, 0.5, 1],
        [-1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [-1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, 1, 1],
        [-1, 1, 1],
        [-1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [-1, -1, -1],
        [1, -1, -1],
        [1, -1, -1],
        [1, -1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [-1, -1, -1],
        [1, 1, -1],
        ])
    """

    done = False
    episode_reward = 0
    episode_energy_comsumption = 0
    step_counter = 0
    env.reset()
    while not done:
    # for i in range(len(actions)):
        # action = actions[step_counter%len(actions)]
        action = actions[(step_counter+0)%len(actions)]
        # action = actions[len(actions) - (step_counter+2)%len(actions) -1]
        #print('action:', step_counter%len(action_list))
        # print('i =', step_counter)
        # print(action)
        obs, reward, done, info = env.step(action)
        # print(reward)
        #print('reward:', reward)
        step_counter += 1
        episode_reward += reward
        episode_energy_comsumption += info['energy_consumption'].sum()
        if done == True:
            break

    print('final position ', info['center'][0])
    print('Energy consumption:', episode_energy_comsumption)
    print('Episode Reward:', episode_reward)


if __name__ == '__main__':
    main()
