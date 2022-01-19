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
    create_new_model = True
    params = {
            'swimmer_type':       20,
            'on_record':          False,
<<<<<<< HEAD
            'action_interval':    0.9,
            'max_length':         1.9,
=======
            'action_interval':    0.3,
            'max_length':         1.3,
>>>>>>> 973de97170e8dd41c0a42ebe8d0f4182ffc01a18
            'consider_energy':    True,
            'random_init_states': False
            }
    df = pd.read_csv(f'sim/analysis/data/characteristic_values/type{params["swimmer_type"]}/displacement_energy.csv')
    ref = df[(df['action_interval'] == params['action_interval']) & (df['max_arm_length'] == params['max_length'])]
    params['displacement_gain'] = 1.0 / ref['onestep_displacement'].values[0]
    params['energy_gain'] = 1.0 / ref['onestep_energyconsumption'].values[0]
    """"""""""""""""""""
    " Hyper Parameters "
    """"""""""""""""""""
    n_envs     = 16
    time_steps = int(2_000_000)
    epoch      = 10
    
    """"""""""""""""""""
    " Learning Setting "
    """"""""""""""""""""
    multi_process    = True
    save_model       = True

    if params['consider_energy']:
        load_model_name = f'ppo' \
                f'_env{n_envs}' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_considerEnergy' \
                f'_20220115_135327'
    else:
        load_model_name = f'ppo' \
                f'_env{n_envs}' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_notConsiderEnergy' \
                f'_20220113_003402'


    """"""""""""""""""""
    " Log Setting      "
    """"""""""""""""""""
    now = datetime.datetime.now()
    if params['consider_energy']:
        if params['random_init_states']:
            log_save_dir = f'./rl/logs/' \
                    f'random_init_states/' \
                    f'type_{params["swimmer_type"]}/' \
                    f'interval{params["action_interval"]}' \
                    f'_maxlength{params["max_length"]}/'
            os.makedirs(log_save_dir, exist_ok=True)
    
            model_save_dir = f'./rl/trained_models/' \
                    f'random_init_states/' \
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
            log_save_dir = f'./rl/logs/' \
                    f'const_init_states/' \
                    f'type_{params["swimmer_type"]}/' \
                    f'interval{params["action_interval"]}' \
                    f'_maxlength{params["max_length"]}/'
            os.makedirs(log_save_dir, exist_ok=True)
    
            model_save_dir = f'./rl/trained_models/' \
                    f'const_init_states/' \
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
        if params['random_init_states']:
            log_save_dir = f'./rl/logs/' \
                    f'random_init_states/' \
                    f'type_{params["swimmer_type"]}/' \
                    f'interval{params["action_interval"]}' \
                    f'_maxlength{params["max_length"]}/'
            os.makedirs(log_save_dir, exist_ok=True)

            model_save_dir = f'./rl/trained_models/' \
                    f'random_init_states/' \
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
            log_save_dir = f'./rl/logs/' \
                    f'const_init_states/' \
                    f'type_{params["swimmer_type"]}/' \
                    f'interval{params["action_interval"]}' \
                    f'_maxlength{params["max_length"]}/'
            os.makedirs(log_save_dir, exist_ok=True)
    
            model_save_dir = f'./rl/trained_models/' \
                    f'const_init_states/' \
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
                        random_init_states=params['random_init_states']
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
                learning_rate=0.0008,
                n_steps=2048,
                batch_size=64,
                n_epochs=10,
                gamma=0.99**params['action_interval'],
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
                random_init_states=params['random_init_states']
                )
            )

    """""""""""""""
    "   TESTING   "
    """""""""""""""
    testModel(model, params)
    print('*'*10, ' EVALUATING ', '*'*10)
    mean_reward, std_reward = evaluate_policy(model, 
            eval_env, n_eval_episodes=1, deterministic=True)
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
                eval_env, n_eval_episodes=1, deterministic=True)
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
                random_init_states=params['random_init_states']
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
