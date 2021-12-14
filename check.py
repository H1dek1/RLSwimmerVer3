#!/usr/bin/env python3
import gym
import skeleton_swimmer_env

env = gym.make(
        'SkeletonSwimmer-v0',
        isRecord=True,
        swimmer_type=10,
        action_interval=1.5,
        max_arm_length=1.5,
        reward_gain=1.0,
        penalty_gain=1.0,
        epsilon=0.0
        )

env.test()
