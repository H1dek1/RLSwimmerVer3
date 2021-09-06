#!/usr/bin/env python3
import numpy as np
from skeleton_swimmer import SkeletonSwimmer

def main():
    env = SkeletonSwimmer(10, False, 2.0, 1.5)
    print(env.getNumActions())
    print(env.getNumStates())
    print(env)
    obs = env.reset()
    print('obs')
    print(type(obs))
    print(obs)
    actions = np.array([0.5, -0.5])
    obs, reward, done, _ = env.step(actions)
    print(obs)
    print(type(obs))
    print('reward', reward)
    print('Done', done)


if __name__ == '__main__':
    main()

