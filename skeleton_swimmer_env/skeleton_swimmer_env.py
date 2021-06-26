from skeleton_swimmer_env.skeleton_swimmer import SkeletonSwimmer
import gym
import numpy as np

class SkeletonSwimmerEnv(gym.Env):
    def __init__(self, isRecord=False, swimmer_type=10, action_period=1, max_arm_length=0.5):
        self.swimmer = SkeletonSwimmer(swimmer_type, isRecord, action_period, max_arm_length)
        self.n_states = self.swimmer.getNumStates()
        self.n_actions = self.swimmer.getNumActions()
        #print(self.n_states)
        #print(self.n_actions)
        #self.action_space = gym.spaces.Box(
        #        low=-1,
        #        high=1,
        #        shape=(self.n_actions,),
        #        dtype=np.float32)
        #self.observation_space = gym.spaces.Box(
        #        low=-5,
        #        high=5,
        #        shape=(self.n_states,),
        #        dtype=np.float32)

    def reset(self):
        return np.array(self.swimmer.reset())

    def step(self, action):
        obs, reward, done, _ = self.swimmer.step(action)
        return np.array(obs), reward, done, {}

    def test(self):
        integer = self.swimmer.getSwimmerType()
        print('swimmer type: ', integer)
        obs = np.array(self.swimmer.reset())
        print('In python, obs=', obs)
        print(type(obs))
        print('step function')
        action = np.array([0.5, 1.0])
        obs, reward, done, _ = self.swimmer.step(action)
        print('obs', obs)
        print('reward', reward)
        print('done', done)

