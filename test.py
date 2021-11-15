#!/usr/bin/env python3
import sys
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
            'swimmer_type':    20,
            'is_record' :      False,
            'action_interval': 0.7,   # 0.5 ~ 30
            'max_length':      1.7,   # 0.1 ~ 0.8
            }

    if args.mode == 'evaluate':
        print('evaluate')
    elif args.mode == 'simulate':
        print('simulate')
        params['is_record'] = True
    else:
        print('Wrong Value')
        sys.exit(0)

    """
    Cunstruct Env
    """
    env = Monitor(gym.make('SkeletonSwimmer-v0',
            isRecord=params['is_record'],
            swimmer_type=params['swimmer_type'],
            action_period=params['action_interval'],
            max_arm_length=params['max_length'],
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
    done = False
    obs = env.reset()
    # for i in range(1):
    while(done == False):
        action, _states = model.predict(obs, deterministic=deterministic)
        print(action)
        obs, reward, done, _ = env.step(action)
        epi_reward += reward
        if done == True: break

    print('episode reward is ', epi_reward)
    #with open('learned_result_type{}.csv'.format(swimmer_type), mode='a') as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerow([loadtime, epi_reward])



if __name__ == '__main__':
    main()
