#!/usr/bin/env python3

import numpy as np
import gym
import skeleton_swimmer_env

def main():
    params = {
            'swimmer_type':      20,
            'on_record':         True,
            'action_interval':   0.6,
            'max_length':        1.9,
            'reward_gain':       1.0,
            'penalty_gain':      1.0,
            'epsilon':           0.0,
            'reward_per_energy': False,
            }

    env = gym.make(
            'SkeletonSwimmer-v0',
            onRecord=params['on_record'],
            swimmer_type=params['swimmer_type'],
            action_interval=params['action_interval'],
            max_arm_length=params['max_length'],
            reward_gain=params['reward_gain'],
            penalty_gain=params['penalty_gain'],
            epsilon=params['epsilon'],
            reward_per_energy=params['reward_per_energy'],
            )

    actions0 = [
            [-1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0,  1.0, -1.0],
            [-1.0,  1.0, -1.0],
            ]
    actions = np.loadtxt('swimming_method/type20/c.csv', delimiter=',')
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
