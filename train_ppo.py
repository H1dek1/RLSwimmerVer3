#!/usr/bin/env python3
import datetime
import os 
import gym
import numpy as np
import pandas as pd
import skeleton_swimmer_env

from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import PPO

def main():
    """"""""""""""""""""""""""
    " Environment Parameters "
    """"""""""""""""""""""""""
    params = {
            'swimmer_type':      202,
            'on_record':         False,
            'action_interval':   0.7,
            'max_length':        1.7,
            'consider_energy':   False,
            }
    df = pd.read_csv(f'sim/analysis/phase_diagram/characteristic_values/type{params["swimmer_type"]}/displacement_energy.csv')
    ref = df[(df['action_interval'] == params['action_interval']) & (df['max_arm_length'] == params['max_length'])]
    params['displacement_gain'] = 1.0 / ref['onestep_displacement'].values[0]
    params['energy_gain'] = 1.0 / ref['onestep_energyconsumption'].values[0]
    """"""""""""""""""""
    " Hyper Parameters "
    """"""""""""""""""""
    n_envs     = 16
    time_steps = int(2_000_000)
    epoch      = 9
    
    """"""""""""""""""""
    " Learning Setting "
    """"""""""""""""""""
    multi_process    = True
    create_new_model = True
    save_model       = True
    if params['consider_energy']:
        load_model_name = f'ppo' \
                f'_env{n_envs}' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_considerEnergy' \
                f'_20211216_023526'
    else:
        load_model_name = f'ppo' \
                f'_env{n_envs}' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_notConsiderEnergy' \
                f'_20211228_125408'


    """"""""""""""""""""
    " Log Setting      "
    """"""""""""""""""""

    log_save_dir = f'./rl/logs/' \
            f'type_{params["swimmer_type"]}/' \
            f'interval{params["action_interval"]}' \
            f'_maxlength{params["max_length"]}/'
    os.makedirs(log_save_dir, exist_ok=True)

    now = datetime.datetime.now()
    if params['consider_energy']:
        model_save_dir = f'./rl/trained_models/' \
                f'type_{params["swimmer_type"]}/' \
                f'consider_energy/' \
                f'interval{params["action_interval"]}' \
                f'_maxlength{params["max_length"]}/'
        os.makedirs(model_save_dir, exist_ok=True)

        model_name = f'ppo_env{n_envs}' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_considerEnergy_' \
                + now.strftime('%Y%m%d_%H%M%S')
    else:
        model_save_dir = f'./rl/trained_models/' \
                f'type_{params["swimmer_type"]}/' \
                f'not_consider_energy/' \
                f'interval{params["action_interval"]}' \
                f'_maxlength{params["max_length"]}/'
        os.makedirs(model_save_dir, exist_ok=True)

        model_name = f'ppo_env{n_envs}' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_notConsiderEnergy_' \
                + now.strftime('%Y%m%d_%H%M%S')

    """"""""""""""""""""
    " Constructing Env "
    """"""""""""""""""""
    if multi_process:
        env = SubprocVecEnv(
                [lambda: Monitor(
                    gym.make(
                        'SkeletonSwimmer-v0', 
                        onRecord=params['on_record'], 
                        swimmer_type=params['swimmer_type'], 
                        action_interval=params['action_interval'], 
                        max_arm_length=params['max_length'],
                        displacement_gain=params['displacement_gain'],
                        energy_gain=params['energy_gain'],
                        consider_energy=params['consider_energy'],
                        ), 
                    log_save_dir) for i in range(n_envs)], 
                start_method='spawn')
    else:
        env = make_vec_env('SkeletonSwimmer-v0',
                n_envs=n_envs,
                env_kwargs=dict(
                    onRecord=params['on_record'], 
                    swimmer_type=params['swimmer_type'], 
                    action_interval=params['action_interval'], 
                    max_arm_length=params['max_length'],
                    displacement_gain=params['displacement_gain'],
                    energy_gain=params['energy_gain'],
                    consider_energy=params['consider_energy'],
                    ),
                monitor_dir=(log_save_dir+model_name+'_monitor'))


    """""""""""""""""""""
    " Constructing Model"
    """""""""""""""""""""
    if(create_new_model):
        """ New Model
        """
        model = PPO(
                policy='MlpPolicy',
                env=env,
                learning_rate=0.0003,
                n_steps=2048,
                batch_size=64,
                n_epochs=10,
                gamma=0.99,
                gae_lambda=0.95,
                clip_range=0.2,
                clip_range_vf=None,
                ent_coef=0.0,
                vf_coef=0.5,
                max_grad_norm=0.5,
                use_sde=True,
                sde_sample_freq=4,
                target_kl=None,
                tensorboard_log=log_save_dir,
                create_eval_env=False,
                policy_kwargs=None,
                verbose=0,
                seed=None,
                device='cpu',
                _init_setup_model=True
                )
    else:
        """ Loading Model
        """
        model = PPO.load(
                model_save_dir+load_model_name,
                tensorboard_log=log_save_dir)
        model.set_env(env)

    """""""""""""""""""""""
    " Env for Evaluation  "
    """""""""""""""""""""""
    eval_env = Monitor(
            gym.make(
                'SkeletonSwimmer-v0',
                onRecord=params['on_record'],
                swimmer_type=params['swimmer_type'],
                action_interval=params['action_interval'],
                max_arm_length=params['max_length'],
                displacement_gain=params['displacement_gain'],
                energy_gain=params['energy_gain'],
                consider_energy=params['consider_energy'],
                )
            )

    """""""""""""""
    "   TESTING   "
    """""""""""""""
    testModel(model, params)
    print('*'*10, ' EVALUATING ', '*'*10)
    mean_reward, std_reward = evaluate_policy(model, 
            eval_env, n_eval_episodes=1, deterministic=False)
    print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')
    max_score = mean_reward

    """""""""""""""""
    "    TRAINING   "
    """""""""""""""""
    print('*'*10, ' START ', '*'*10)
    for i in range(epoch):
        print('*'*10, ' LEARNING ', '*'*10)
        print('Epoch:', i)
        if i == 0:
            model.learn(
                    total_timesteps=int(time_steps), 
                    tb_log_name=model_name,
                    reset_num_timesteps=True)
        else:
            model.learn(
                    total_timesteps=int(time_steps), 
                    tb_log_name=model_name,
                    reset_num_timesteps=False)
        testModel(model, params)

        print('*'*10, ' EVALUATING ', '*'*10)
        mean_reward, std_reward = evaluate_policy(model, 
                eval_env, n_eval_episodes=5, deterministic=True)
        print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')

        if save_model:
            print('*'*10, ' SAVING MODEL ', '*'*10)
            model.save(model_save_dir+model_name)
            if mean_reward > max_score:
                print('update best model')
                model.save(model_save_dir+model_name+'_best')
                max_score = mean_reward


def testModel(model, params):
    print('*'*10, ' TEST MODEL ', '*'*10)

    test_env = Monitor(
            gym.make(
                'SkeletonSwimmer-v0',
                onRecord=params['on_record'],
                swimmer_type=params['swimmer_type'],
                action_interval=params['action_interval'],
                max_arm_length=params['max_length'],
                displacement_gain=params['displacement_gain'],
                energy_gain=params['energy_gain'],
                consider_energy=params['consider_energy'],
                )
            )

    obs = test_env.reset()
    for i in range(50):
        action, _states = model.predict(obs, deterministic=True)
        print(action)
        obs, reward, done, info = test_env.step(action)
        if done: break


if __name__ == '__main__':
    main()
