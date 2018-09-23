import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='RandomWalk-v0',
    entry_points='gym_random_walk.envs:RandomWalkEnv',
)

