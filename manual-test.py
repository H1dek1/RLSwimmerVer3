#!/usr/bin/env python3

import numpy as np
import gym

import skeleton_swimmer_env

def main():
    is_record = True
    swimmer_type = 20
    action_period = 1.0
    max_arm_length = 1.1

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
    actionA = [
            [ 1.0, -1.0, -1.0],
            [ 1.0, -1.0,  1.0],
            [-1.0,  1.0, -1.0],
            [-1.0,  1.0,  1.0],
            ]
    actionB = [
            [ 1.0, -1.0, -1.0],
            #[ 1.0, -1.0, -1.0],
            #[ 1.0, -1.0, -1.0],

            [ 1.0, -1.0,  1.0],
            #[ 1.0, -1.0,  1.0],
            #[ 1.0, -1.0,  1.0],

            [-1.0, -1.0,  1.0],
            #[-1.0, -1.0,  1.0],
            #[-1.0, -1.0,  1.0],

            [-1.0, -1.0, -1.0],
            #[-1.0, -1.0, -1.0],
            #[-1.0, -1.0, -1.0],

            [-1.0,  1.0, -1.0],
            #[-1.0,  1.0, -1.0],
            #[-1.0,  1.0, -1.0],

            [-1.0,  1.0,  1.0],
            #[-1.0,  1.0,  1.0],
            #[-1.0,  1.0,  1.0],

            [-1.0, -1.0,  1.0],
            #[-1.0, -1.0,  1.0],
            #[-1.0, -1.0,  1.0],

            [-1.0, -1.0, -1.0],
            #[-1.0, -1.0, -1.0],
            #[-1.0, -1.0, -1.0],
            ]
    # triangle (0.2, 1.5) 1
    actions = [
            [ 1.,  1., -1.],
            [-1.,  1., -1.],
            [-1.,  1.,  1.],
            [-1.,  1.,  1.],
            [-1., -1.,  1.],
            [-1.,        -1.,        -0.5775105],
            [-1., -1., -1.],
            [ 1., -1., -1.],
            [ 1., -1., -1.],
            [ 1., -1.,  1.],
            [ 1., -1.,  1.],
            [-1., -1.,  1.],
            [-1., -1.,  1.],
            [-1., -1., -1.],
            [-1., -1., -1.],
            ]
    # triangle (0.2, 1.5) 2
    actions = [
            [ 1., -1., -1.],
            [ 1., -1., -1.],
            [ 1., -1.,  1.],
            [ 1., -1.,  1.],
            [-1., -1.,  1.],
            [-1., -1.,  1.],
            [-1., -1., -1.],
            [-1., -1., -1.],
            [ 1.,  1., -1.],
            [-1.,  1., -1.],
            [-1.,  1.,  1.],
            [-1.,  1.,  1.],
            [-1., -1.,  1.],
            [-1., -1.,  -0.7],
            [-1., -1., -1.],
            ]

    action_list = actionA
    done = False
    episode_reward = 0
    step_counter = 0
    env.reset()
    while not done:
    #for i in range(100):
        print('*'*40)
        print('i =', step_counter)
        action = action_list[step_counter%len(action_list)]
        print('action:', step_counter%len(action_list))
        obs, reward, done, _ = env.step(action)
        #print('reward:', reward)
        step_counter += 1
        episode_reward += reward

    print('Episode Reward:', episode_reward)


if __name__ == '__main__':
    main()
