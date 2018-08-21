import logging
from gym_soccer.envs.soccer_env import SoccerEnv

logger = logging.getLogger(__name__)

class SoccerMatchEnv(SoccerEnv):
    def __init__(self):
        super(self.__class__, self).__init__()

    def _configure_environment(self):
        super(self.__class__, self)._start_hfo_server(defense_npcs=3,
                                                      offense_npcs=2)
