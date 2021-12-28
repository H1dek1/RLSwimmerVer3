#!/usr/bin/env python3

import numpy as np
import gym
import skeleton_swimmer_env

def main():
    params = {
            'swimmer_type':      20,
<<<<<<< HEAD
            'on_record':         True,
            'action_interval':   0.6,
            'max_length':        1.9,
            'reward_gain':       1.0,
            'penalty_gain':      1.0,
            'epsilon':           0.0,
            'reward_per_energy': False,
=======
            'on_record':         False,
            'action_interval':   0.6,
            'max_length':        1.6,
            'consider_energy':   False,
>>>>>>> b6fd98002008315adcf21246e751de1491560ca9
            }
    df = pd.read_csv('sim/analysis/phase_diagram/characteristic_values/type20/displacement_energy.csv')
    ref = df[(df['action_interval'] == params['action_interval']) & (df['max_arm_length'] == params['max_length'])]
    params['displacement_gain'] = 1.0 / ref['onestep_displacement'].values[0]
    params['energy_gain'] = 1.0 / ref['onestep_energyconsumption'].values[0]

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

    actions0 = [
            [-1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0,  1.0, -1.0],
            [-1.0,  1.0, -1.0],
            ]
<<<<<<< HEAD
    actions = np.loadtxt('swimming_method/type20/c.csv', delimiter=',')
=======
    actions = np.loadtxt('swimming_method/type20/a.csv', delimiter=',')
>>>>>>> b6fd98002008315adcf21246e751de1491560ca9
    # actions *= 0.1

    done = False
    episode_reward = 0
    step_counter = 0
    env.reset()
    while not done:
    # for i in range(10):
        action = actions[step_counter%len(actions)]
        #print('action:', step_counter%len(action_list))
        # print('i =', step_counter)
        # print(action)
        obs, reward, done, info = env.step(action)
        # print(reward)
        #print('reward:', reward)
        step_counter += 1
        episode_reward += reward
        if done == True:
            break

    print('final position ', info)
    print('Episode Reward:', episode_reward)


if __name__ == '__main__':
    main()
