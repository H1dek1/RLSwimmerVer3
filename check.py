#!/usr/bin/env python3
import gym
import skeleton_swimmer_env

env = gym.make('SkeletonSwimmer-v0', isRecord=True, swimmer_type=10, action_period=1, max_arm_length=0.5)
