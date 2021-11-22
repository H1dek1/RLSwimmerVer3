#!/usr/bin/env python3

import numpy as np
import gym

import skeleton_swimmer_env

def main():
    is_record = True
    swimmer_type = 20
    action_period  = 0.1
    max_arm_length = 1.1

    env = gym.make('SkeletonSwimmer-v0', 
            isRecord=is_record, 
            swimmer_type=int(swimmer_type), 
            action_period=action_period, 
            max_arm_length=max_arm_length)

    actions0 = [
            [-1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0,  1.0, -1.0],
            [-1.0,  1.0, -1.0],
            ]
    actions1 = np.loadtxt('sim/optimal_action_pattern/radius0.1/type_20/009_long.csv', delimiter=',')
    done = False
    episode_reward = 0
    step_counter = 0
    env.reset()
    while not done:
        if step_counter < 0:
            action = actions0[step_counter%len(actions0)]
        else:
            action = actions1[step_counter%len(actions1)]
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
