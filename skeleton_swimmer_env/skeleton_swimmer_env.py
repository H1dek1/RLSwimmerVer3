from skeleton_swimmer_env.skeleton_swimmer import SkeletonSwimmer
import gym
import numpy as np

class SkeletonSwimmerEnv(gym.Env):
    def __init__(self, onRecord=False, swimmer_type=10, action_interval=0.5, max_arm_length=1.5, displacement_gain=1.0, energy_gain=1.0, consider_energy=False):

        self.swimmer = SkeletonSwimmer(
                swimmer_type,
                onRecord,
                action_interval, 
                max_arm_length,
                displacement_gain,
                energy_gain,
                consider_energy)

        self._swimmer_type = swimmer_type
        self.n_states = self.swimmer.getNumStates()
        self.n_actions = self.swimmer.getNumActions()

        self.action_space = gym.spaces.Box(
                low=-1.0,
                high=1.0,
                shape=(self.n_actions,),
                dtype=np.float32)
        self.observation_space = gym.spaces.Box(
                low=-10.0,
                high=10.0,
                shape=(self.n_states,),
                dtype=np.float32)

    def reset(self):
        return self.swimmer.reset()

    def step(self, action):
        return self.swimmer.step(action)

    def get_type(self):
        return self._swimmer_type

    def test(self):
        integer = self.get_type()
        print('swimmer type: ', integer)
        obs = self.reset()
        print('In python, obs=', obs)
        print(type(obs))
        print('step function')
        action = np.array([0.0, 1.0])
        obs, reward, done, info = self.step(action)
        print('obs', obs)
        print('reward', reward)
        print('done', done)
        print('info', info)
        print('info type', type(info))

