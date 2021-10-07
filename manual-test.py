#!/usr/bin/env python3

import numpy as np
import gym

import skeleton_swimmer_env

def main():
    is_record = True
    swimmer_type = 20
    action_period = 0.2
    max_arm_length = 1.9

    env = gym.make('SkeletonSwimmer-v0', 
            isRecord=is_record, 
            swimmer_type=int(swimmer_type), 
            action_period=action_period, 
            max_arm_length=max_arm_length)

    actions = [
            [ 1.0,  1.0],
            [-1.0, -1.0],
            ]
    actions = [
            [ 1.0, -1.0],
            [ 1.0,  1.0],
            [-1.0,  1.0],
            [-1.0, -1.0],
            ]
    actions = [
            [ 1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],

            [ 1.0, -1.0,  1.0],
            [ 1.0, -1.0,  1.0],
            [ 1.0, -1.0,  1.0],

            [-1.0, -1.0,  1.0],
            [-1.0, -1.0,  1.0],
            [-1.0, -1.0,  1.0],

            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0],

            [-1.0,  1.0, -1.0],
            [-1.0,  1.0, -1.0],
            [-1.0,  1.0, -1.0],

            [-1.0,  1.0,  1.0],
            [-1.0,  1.0,  1.0],
            [-1.0,  1.0,  1.0],

            [-1.0, -1.0,  1.0],
            [-1.0, -1.0,  1.0],
            [-1.0, -1.0,  1.0],

            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0],
            ]

    done = False
    episode_reward = 0
    step_counter = 0
    env.reset()
    while not done:
        print('*'*40)
        print('i =', step_counter)
        action = actions[step_counter%len(actions)]
        print('action:', action)
        obs, reward, done, _ = env.step(action)
        print('reward:', reward)
        step_counter += 1
        episode_reward += reward

    print('Episode Reward:', episode_reward)


if __name__ == '__main__':
    main()
