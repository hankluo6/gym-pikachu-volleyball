import gym
import numpy as np

from gym import spaces
from gym.utils.renderer import Renderer

from typing import Tuple, Union, Optional

from gym_pikachu_volleyball.envs.engine import Engine
from gym_pikachu_volleyball.envs.common import convert_to_user_input
from gym_pikachu_volleyball.envs.constants import GROUND_HALF_WIDTH

class PikachuVolleyballEnv(gym.Env):

    metadata = {"render_modes": ["human", ]}

    def __init__(self, is_player1_computer: bool, is_player2_computer: bool, render_mode: str):
        super(PikachuVolleyballEnv, self).__init__()

        observation_size = (304, 432, 3)
        self.observation_space = spaces.Box(
                low = np.zeros(observation_size), 
                high = 255 * np.ones(observation_size),
                dtype = np.uint8)

        self.engine = Engine(is_player1_computer, is_player2_computer)
        self.engine.create_viewer(render_mode)

        self.render_mode = render_mode
        self._renderer = Renderer(self.render_mode, self.engine.render)
   
    def render(self):
        return self._renderer.get_renders()

    def close(self) -> None:
        self.engine.close()