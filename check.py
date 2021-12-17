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

env.reset()
_, reward, done, info = env.step([0.0, 0.0, 0.0])

initial_position = info['center']
_, reward, done, info = env.step([0.0, 0.0, 1.0])
final_position = info['center']

displacement = final_position - initial_position
print('vector', displacement)
print('distance', np.linalg.norm(displacement))
print('energy', sum(info['energy_penalty']))
