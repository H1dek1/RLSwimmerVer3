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
    swimmer_type   = int(20)
    load_time      = 0.2
    max_arm_length = 1.9
    reward_gain    = 100.0
    n_envs         = 16
    args = parser.parse_args()

    if args.mode == 'evaluate':
        print('evaluate')
        is_record = False
    elif args.mode == 'simulate':
        print('simulate')
        is_record = False
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
    load_dir = f'./rl/trained_models/' \
            f'type_{swimmer_type}/' \
            f'period{load_time}' \
            f'_length{max_arm_length}/'
    model_name = f'ppo_type{swimmer_type}' \
            f'_actionperiod{load_time}' \
            f'_maxlength{max_arm_length}' \
            f'_rewardgain{reward_gain}' \
            f'_env{n_envs}' \
            f'_20210917_154115_best'

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
    step_counter = 0
    while(done == False):
        action, _states = model.predict(obs, deterministic=kwargs['deterministic'])
        #print('action')
        print(action)
        obs, reward, done, info = env.step(action)
        #print('reward')
        #print(reward)
        #print('*'*40)
        epi_reward += reward
        #if step_counter == 100: break
        if done == True: break
        step_counter += 1

    print('final position ', info)
    print('episode reward is ', epi_reward)
    #with open('learned_result_type{}.csv'.format(swimmer_type), mode='a') as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerow([load_time, epi_reward])



if __name__ == '__main__':
    main()
