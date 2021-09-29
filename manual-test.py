#!/usr/bin/env python3

import numpy as np

import skeleton_swimmer_env

def main():
    is_record = True
    swimmer_type = 10
    action_period = 1.0
    max_arm_length = 1.9

    env = gym.make('SkeletonSwimmer-v0', 
            isRecord=is_record, 
            swimmer_type=int(swimmer_type), 
            action_period=action_period, 
            max_arm_length=max_arm_length)

if __name__ == '__main__':
    main()
