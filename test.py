#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt
from distutils.util import strtobool
import argparse
import gym
import csv

from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import PPO, SAC

import skeleton_swimmer_env

parser = argparse.ArgumentParser(description=
        'This program is for evaluating or simulating trained model. 2 arguments required.')
parser.add_argument('--mode', choices=['evaluate', 'simulate'], 
        help='"evaluate" or "simulate"', required=True)
parser.add_argument('--model', type=str, 
        help='Learned model path', required=True)
parser.add_argument('--deterministic', type=strtobool, 
        help='Whether choose actions deterministic or not. Default value is False', default=False)

def main():
    args = parser.parse_args()
    """"""""""""""""""""""""""
    " Environment Parameters "
    """"""""""""""""""""""""""
    params = {
            'swimmer_type':      20,
            'is_record' :        False,
            'action_interval':   0.3,   # 0.5 ~ 30
            'max_length':        1.3,   # 0.1 ~ 0.9
            'reward_gain':       300,
            'penalty_gain':      1.0,
            'epsilon':           0.0,
            'reward_per_energy': True,
            }

    if args.mode == 'evaluate':
        print('evaluate')
    elif args.mode == 'simulate':
        print('simulate')
        # params['is_record'] = True
    else:
        print('Wrong Value')
        sys.exit(0)

    """
    Cunstruct Env
    """
    env = Monitor(gym.make('SkeletonSwimmer-v0',
            isRecord=params['is_record'],
            swimmer_type=params['swimmer_type'],
            action_interval=params['action_interval'],
            max_arm_length=params['max_length'],
            reward_gain=params['reward_gain'],
            penalty_gain=params['penalty_gain'],
            epsilon=params['epsilon'],
            reward_per_energy=params['reward_per_energy'],
            ))

    """
    Load RL Model
    """
    model = PPO.load(args.model)
    # model = SAC.load(args.model)

    """
    Run
    """
    if args.mode == 'evaluate':
        print('*'*10, ' EVALUATING ', '*'*10)
        mean_reward, std_reward = evaluate_policy(model,
                env, n_eval_episodes=1, deterministic=args.deterministic)
        print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')

    elif args.mode == 'simulate':
        simulate(env, model, args.deterministic)


def simulate(env, model, deterministic):
    print('*'*10, ' SIMULATING ', '*'*10)
    epi_reward = 0
    displacement_list = []
    penalty_list = []
    reward_list = []
    done = False
    obs = env.reset()
    # for i in range(1):
    while(done == False):
        action, _states = model.predict(obs, deterministic=deterministic)
        print(action)
        obs, reward, done, info = env.step(action)
        epi_reward += reward
        displacement_list.append(info['displacement'][0])
        penalty_list.append(info['energy_penalty'].sum())
        reward_list.append(reward)
        if done == True: break

    # displacement_list /= abs(np.median(displacement_list))
    # penalty_list      /= abs(np.median(penalty_list))

    displacement_list = np.array(displacement_list)
    penalty_list = np.array(penalty_list)
    reward_list = np.array(reward_list)

    print('episode reward is', epi_reward)

    print('displacement')
    print('mean      ', np.mean(displacement_list))
    print('abs mean  ', np.mean(abs(displacement_list)))
    print('median    ', np.median(displacement_list))
    print('abs median', np.median(abs(displacement_list)))
    print('var       ', np.var(displacement_list))
    print('min       ', np.min(displacement_list))
    print('max       ', np.max(displacement_list))

    print('penalty')
    print('mean  ', np.mean(penalty_list))
    print('median', np.median(penalty_list))
    print('var   ', np.var(penalty_list))
    print('min   ', np.min(penalty_list))
    print('max   ', np.max(penalty_list))

    print('reward')
    print('mean      ', np.mean(reward_list))
    print('abs mean  ', np.mean(abs(reward_list)))
    print('median    ', np.median(reward_list))
    print('abs median', np.median(abs(reward_list)))
    print('var       ', np.var(reward_list))
    print('min       ', np.min(reward_list))
    print('max       ', np.max(reward_list))
    fig, ax = plt.subplots(1, 1)
    ax.plot(range(len(displacement_list)), displacement_list, label='displacement')
    ax.plot(range(len(displacement_list)), penalty_list, label='penalty')
    ax.legend()
    # plt.show()
    #with open('learned_result_type{}.csv'.format(swimmer_type), mode='a') as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerow([loadtime, epi_reward])



if __name__ == '__main__':
    main()
