import gym
from gym import spaces, utils
from gym.utils import seeding


class RandomWalkEnv(gym.Env):

    def __init__(self, n_states, start_state):
        self.n = n_states
        self.start_state = start_state
        self.state = self.start_state
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(self.n)
        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        displacement = self.np_random.choice([-1, 1])
        self.state += displacement
        if self.state == 0:
            reward = 0
            done = True
        elif self.state == 6:
            reward = 1
            done = True
        elif self.state > 0 and self.state < 6:
            reward = 0
            done = False
        return self.state, reward, done, {}

    def reset(self):
        self.state = self.start_state
        return self.state
