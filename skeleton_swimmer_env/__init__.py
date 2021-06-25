from gym.envs.registration import register

register(
        id='SkeletonSwimmer-v0',
        entry_point='skeleton_swimmer_env.skeleton_swimmer:SkeletonSwimmerEnv'
        )
