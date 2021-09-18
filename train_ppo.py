#!/usr/bin/env python3
import datetime
import os 
import gym
import skeleton_swimmer_env

from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import PPO

swimmer_type = int(20)
reward_gain  = 100.0
load_time    = 0.2
max_arm_length = 1.9

def main():
    """"""""""""""""""""
    " Hyper Parameters "
    """"""""""""""""""""
    n_envs     = 16
    time_steps = int(1e+6)
    epoch      = 20
    
    """"""""""""""""""""
    " Learning Setting "
    """"""""""""""""""""
    multi_process    = True
    create_new_model = False
    load_model_name  = f'ppo' \
            f'_type{swimmer_type}' \
            f'_actionperiod{load_time}' \
            f'_maxlength{max_arm_length}' \
            f'_rewardgain{reward_gain}' \
            f'_env{n_envs}' \
            f'_20210916_210258'

    save_model = True

    """"""""""""""""""""
    " Log Setting      "
    """"""""""""""""""""
    model_save_dir = f'./rl/trained_models/type_{swimmer_type}/period{load_time}_length{max_arm_length}/'
    os.makedirs(model_save_dir, exist_ok=True)
    log_dir = f'./rl/logs/type_{swimmer_type}/'
    os.makedirs(log_dir, exist_ok=True)
    now = datetime.datetime.now()
    model_name = f'ppo_type{swimmer_type}_actionperiod{load_time}_maxlength{max_arm_length}_rewardgain{reward_gain}_env{n_envs}_' + now.strftime('%Y%m%d_%H%M%S')

    """"""""""""""""""""
    " Constructing Env "
    """"""""""""""""""""
    if multi_process:
        env = SubprocVecEnv(
                [lambda: Monitor(gym.make('SkeletonSwimmer-v0', 
                    isRecord=False, 
                    swimmer_type=swimmer_type, 
                    action_period=load_time, 
                    max_arm_length=max_arm_length), 
                log_dir) for i in range(n_envs)], 
                start_method='spawn')
    else:
        env = make_vec_env('SkeletonSwimmer-v0',
                n_envs=n_envs,
                env_kwargs=dict(
                    isRecord=False, 
                    swimmer_type=swimmer_type, 
                    action_period=action_period, 
                    max_arm_length=max_arm_length),
                monitor_dir=(log_dir+model_name+'_monitor'))


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
                tensorboard_log=log_dir,
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
        model = PPO.load(model_save_dir+load_model_name, tensorboard_log=log_dir)
        model.set_env(env)

    """""""""""""""""""""""
    " Env for Evaluation  "
    """""""""""""""""""""""
    eval_env = Monitor(gym.make('SkeletonSwimmer-v0', 
            swimmer_type=swimmer_type, isRecord=False, action_period=load_time, max_arm_length=max_arm_length))

    """""""""""""""
    "   TESTING   "
    """""""""""""""
    testModel(model)
    print('*'*10, ' EVALUATING ', '*'*10)
    mean_reward, std_reward = evaluate_policy(model, 
            eval_env, n_eval_episodes=2, deterministic=True)
    print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')
    max_score = mean_reward

    """""""""""""""""
    "    TRAINING   "
    """""""""""""""""
    print('*'*10, ' START ', '*'*10)
    for _ in range(epoch):
        print('*'*10, ' LEARNING ', '*'*10)
        model.learn(total_timesteps=int(time_steps), 
                tb_log_name=model_name)
        testModel(model)
        print('*'*10, ' EVALUATING ', '*'*10)
        mean_reward, std_reward = evaluate_policy(model, 
                eval_env, n_eval_episodes=5)
        print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')

        if save_model == True and mean_reward > max_score:
            print('*'*10, ' SAVING MODEL ', '*'*10)
            model.save(model_save_dir+model_name)
            max_score = mean_reward


def testModel(model):
    print('*'*10, ' TEST MODEL ', '*'*10)
    env = gym.make('SkeletonSwimmer-v0', 
            swimmer_type=swimmer_type, isRecord=False, action_period=load_time, max_arm_length=max_arm_length)

    obs = env.reset()
    for i in range(50):
        action, _states = model.predict(obs, deterministic=True)
        print(action)
        obs, reward, done, _ = env.step(action)
        if done == True: break


if __name__ == '__main__':
    main()
