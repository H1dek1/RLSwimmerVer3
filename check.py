#!/usr/bin/env python3
import numpy as np
import gym
import skeleton_swimmer_env

env = gym.make(
        'SkeletonSwimmer-v0',
        onRecord=False,
        swimmer_type=20,
        action_interval=0.1,
        max_arm_length=1.1,
        displacement_gain=1.0,
        energy_gain=1.0,
        consider_energy=True)

obs = env.reset()
print('obs')
print(obs)

obs, reward, done, info = env.step(env.action_space.sample())
print('obs')
print(obs)
print('reward', reward)
print('done', done)
print('info')
print(info)
