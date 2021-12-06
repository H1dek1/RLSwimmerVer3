#!/usr/bin/env python3

import numpy as np
import gym

import skeleton_swimmer_env

def main():
    params = {
            'swimmer_type':    20,
            'is_record':       False,
            'action_interval': 0.7,
            'max_length':      1.7,
            'reward_gain':     1.0/0.006964,
            'penalty_gain':    1.0/0.9554,
            'epsilon':         0.3,
            }

    env = gym.make(
            'SkeletonSwimmer-v0',
            isRecord=params['is_record'],
            swimmer_type=params['swimmer_type'],
            action_interval=params['action_interval'],
            max_arm_length=params['max_length'],
            reward_gain=params['reward_gain'],
            penalty_gain=params['penalty_gain'],
            epsilon=params['epsilon'],
            )

    actions0 = [
            [-1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0,  1.0, -1.0],
            [-1.0,  1.0, -1.0],
            ]
    actions1 = np.loadtxt('sim/optimal_action_pattern/radius0.1/type_20/009_long.csv', delimiter=',')
    actions2 = [
            [ 1.0,  1.0, -1.0],
            [ 1.0,  1.0,  1.0],
            [-1.0, -1.0,  1.0],
            [-1.0, -1.0, -1.0],
            ]
    actions3 = [
            [-1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0, -1.0,  1.0],
            [-1.0, -1.0,  1.0],
            [-1.0, -1.0, -1.0],
            [-1.0,  1.0, -1.0],
            [-1.0,  1.0,  1.0],
            [-1.0, -1.0,  1.0],
            ]
    actions3 = np.array(actions3)
    actions2 = np.array(actions2)
    actions2 *= 0.1
    actions3 *= 0.63
    done = False
    episode_reward = 0
    step_counter = 0
    env.reset()
    while not done:
        if step_counter < 0:
            action = actions3[step_counter%len(actions3)]
        else:
            action = actions3[step_counter%len(actions3)]
        #print('action:', step_counter%len(action_list))
        print('i =', step_counter)
        print(action)
        obs, reward, done, info = env.step(action)
        #print('reward:', reward)
        step_counter += 1
        episode_reward += reward
        if done == True:
            break

    print('final position ', info)
    print('Episode Reward:', episode_reward)


if __name__ == '__main__':
    main()
