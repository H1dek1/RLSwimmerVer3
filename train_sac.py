#!/usr/bin/env python3
import datetime
import os 
import gym
import skeleton_swimmer_env

from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import SAC

swimmer_type = int(10)
reward_gain  = 100.0
load_time    = 1.0
max_arm_length = 1.1

def main():
    """"""""""""""""""""
    " Hyper Parameters "
    """"""""""""""""""""
    time_steps = int(1e+6)
    epoch      = 9
    
    """"""""""""""""""""
    " Learning Setting "
    """"""""""""""""""""
    create_new_model = True
    load_model_name  = f'sac' \
            f'_type{swimmer_type}' \
            f'_actionperiod{load_time}' \
            f'_maxlength{max_arm_length}' \
            f'_rewardgain{reward_gain}' \
            f'_20210922_150935'

    save_model = True

    """"""""""""""""""""
    " Log Setting      "
    """"""""""""""""""""
    model_save_dir = f'./rl/trained_models/type_{swimmer_type}/period{load_time}_length{max_arm_length}/'
    os.makedirs(model_save_dir, exist_ok=True)
    log_dir = f'./rl/logs/type_{swimmer_type}/'
    os.makedirs(log_dir, exist_ok=True)
    now = datetime.datetime.now()
    model_name = f'sac_type{swimmer_type}_actionperiod{load_time}_maxlength{max_arm_length}_rewardgain{reward_gain}_' + now.strftime('%Y%m%d_%H%M%S')

    """"""""""""""""""""
    " Constructing Env "
    """"""""""""""""""""
    env = gym.make('SkeletonSwimmer-v0',
            isRecord=False, 
            swimmer_type=swimmer_type,
            action_period=load_time,
            max_arm_length=max_arm_length)


    """""""""""""""""""""
    " Constructing Model"
    """""""""""""""""""""
    if(create_new_model):
        """ New Model
        """
        model = SAC(
                policy='MlpPolicy',
                env=env,
                verbose=0,
                )
    else:
        """ Loading Model
        """
        model = SAC.load(model_save_dir+load_model_name, tensorboard_log=log_dir)
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
