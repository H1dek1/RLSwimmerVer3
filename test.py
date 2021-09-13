#!/usr/bin/env python3
import sys
from distutils.util import strtobool
import argparse
import gym
import csv

from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import PPO

import skeleton_swimmer_env

parser = argparse.ArgumentParser(description=
        'This program is for evaluating or simulating trained model. 2 arguments required.')
parser.add_argument('--mode', choices=['evaluate', 'simulate'], 
        help='"evaluate" or "simulate"', required=True)
parser.add_argument('--deterministic', type=strtobool, 
        help='Whether choose actions deterministic or not. Default value is False', default=False)


def main():
    swimmer_type   = int(10)
    load_time      = 1.0
    max_arm_length = 1.9
    reward_gain    = 30.0
    n_envs         = 16
    args = parser.parse_args()

    if args.mode == 'evaluate':
        print('evaluate')
        is_record = False
    elif args.mode == 'simulate':
        print('simulate')
        is_record = True
    else:
        print('Wrong Value')
        sys.exit(0)

    """
    Cunstruct Env
    """
    env = Monitor(
            gym.make('SkeletonSwimmer-v0', 
                isRecord=is_record, 
                swimmer_type=swimmer_type,
                action_period=load_time,
                max_arm_length=max_arm_length
                )
            )    

    """
    Load RL Model
    """
    load_dir = f'./rl/trained_models/type_{swimmer_type}/period{load_time}_length{max_arm_length}/'
    model_name = f'ppo_type{swimmer_type}_actionperiod{load_time}_maxlength{max_arm_length}_rewardgain{reward_gain}_env{n_envs}_20210913_151322'

    model = PPO.load(path=(load_dir+model_name))

    """
    Run
    """
    if args.mode == 'evaluate':
        print('*'*10, ' EVALUATING ', '*'*10)
        mean_reward, std_reward = evaluate_policy(model,
                env, n_eval_episodes=1, deterministic=args.deterministic)
        print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')

    elif args.mode == 'simulate':
        simulate(env=env, model=model, 
                is_record=is_record,
                swimmer_type=swimmer_type, 
                load_time=load_time,
                max_arm_length=max_arm_length,
                reward_gain=reward_gain,
                deterministic=args.deterministic
                )

def simulate(env, model, **kwargs):
    print('*'*10, ' SIMULATING ', '*'*10)
    env = gym.make('SkeletonSwimmer-v0', 
            isRecord=kwargs['is_record'],
            swimmer_type=kwargs['swimmer_type'],
            action_period=kwargs['load_time'],
            max_arm_length=kwargs['max_arm_length']
            )
    epi_reward = 0

    done = False
    obs = env.reset()
    while(done == False):
        action, _states = model.predict(obs, deterministic=kwargs['deterministic'])
        print(action)
        obs, reward, done, _ = env.step(action)
        epi_reward += reward
        if done == True: break

    print('episode reward is ', epi_reward)
    #with open('learned_result_type{}.csv'.format(swimmer_type), mode='a') as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerow([load_time, epi_reward])



if __name__ == '__main__':
    main()
