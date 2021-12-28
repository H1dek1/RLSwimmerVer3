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

def main():
    """"""""""""""""""""""""""
    " Environment Parameters "
    """"""""""""""""""""""""""
    params = {
            'swimmer_type':    20,
            'on_record':       False,
            'action_interval': 0.1,
            'max_length':      1.1,
            'consider_energy': False
            }
    df = pd.read_csv('sim/analysis/phase_diagram/characteristic_values/type20/displacement_energy.csv')
    ref = df[(df['action_interval'] == params['action_interval']) & (df['max_arm_length'] == params['max_length'])]
    params['displacement_gain'] = 1.0 / ref['onestep_displacement'].values[0]
    params['energy_gain'] = 1.0 / ref['onestep_energyconsumption'].values[0]
    """"""""""""""""""""
    " Hyper Parameters "
    """"""""""""""""""""
    time_steps = int(2_000_000)
    epoch      = 9
    
    """"""""""""""""""""
    " Learning Setting "
    """"""""""""""""""""
    multi_process    = True
    create_new_model = True
    save_model       = True
    if params['consider_energy']:
        load_model_name  = f'sac' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_considerEnergy' \
                f'_20211005_111749'
    else:
        load_model_name  = f'sac' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_notConsiderEnergy' \
                f'_20211005_111749'


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
                f'interval{params["action_interval"]}' \
                f'_maxlength{params["max_length"]}/' \
                f'consider_energy/'
        os.makedirs(model_save_dir, exist_ok=True)
        model_name = f'sac' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_considerEnergy_' \
                + now.strftime('%Y%m%d_%H%M%S')
    else:
        model_save_dir = f'./rl/trained_models/' \
                f'type_{params["swimmer_type"]}/' \
                f'interval{params["action_interval"]}' \
                f'_maxlength{params["max_length"]}/' \
                f'not_consider_energy/'
        os.makedirs(model_save_dir, exist_ok=True)
        model_name = f'sac' \
                f'_displacementgain{params["displacement_gain"]:.2f}' \
                f'_energygain{params["energy_gain"]:.2f}' \
                f'_notConsiderEnergy_' \
                + now.strftime('%Y%m%d_%H%M%S')

    """"""""""""""""""""
    " Constructing Env "
    """"""""""""""""""""
    env = Monitor(
            gym.make(
                'SkeletonSwimmer-v0',
                onRecord=params['on_record'],
                swimmer_type=params['swimmer_type'],
                action_interval=params['action_interval'],
                max_arm_length=params['max_length'],
                displacement_gain=params['displacement_gain'],
                energy_gain=params['energy_gain'],
                consider_energy=params['consider_energy']
                )
            )

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
                tensorboard_log=log_save_dir,
                )
    else:
        """ Loading Model
        """
        model = SAC.load(
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
                consider_energy=params['consider_energy']
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
    for _ in range(epoch):
        print('*'*10, ' LEARNING ', '*'*10)
        model.learn(total_timesteps=int(time_steps), 
                tb_log_name=model_name)
        testModel(model, params)

        print('*'*10, ' EVALUATING ', '*'*10)
        mean_reward, std_reward = evaluate_policy(model, 
                eval_env, n_eval_episodes=5)
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
                consider_energy=params['consider_energy']
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
