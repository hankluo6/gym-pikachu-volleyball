import gymnasium as gym
import numpy as np

from gymnasium import spaces
from typing import Tuple, Union, Optional

from gym_pikachu_volleyball.envs.engine import Engine
from gym_pikachu_volleyball.envs.common import convert_to_user_input
from gym_pikachu_volleyball.envs.constants import GROUND_HALF_WIDTH

class PikachuVolleyballEnv(gym.Env):

    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 25}
    pixel_mode = False
    is_player2_serve = False

    def __init__(self, is_player1_computer: bool, is_player2_computer: bool, render_mode: str):
        super(PikachuVolleyballEnv, self).__init__()

        self.action_space = spaces.Discrete(18)
        
        if self.pixel_mode:
            observation_size = (304, 432, 3)
            self.observation_space = spaces.Box(
                    low = np.zeros(observation_size), 
                    high = 255 * np.ones(observation_size),
                    dtype = np.uint8)
        else:
            observation_size = 10
            high = np.array([np.finfo(np.float32).max] * 10)
            self.observation_space = spaces.Box(-high, high)

        self.engine = Engine(is_player1_computer, is_player2_computer)
        self.engine.create_viewer(render_mode)

        self.render_mode = render_mode
   
    def render(self):
        return self.engine.render(self.render_mode)

    def step(self, action, other_action = None):
        if other_action == None:
            other_action = self.engine.let_computer_decide_user_input(player_id=0)
            converted_action = (other_action, convert_to_user_input(action, 1))
        else:
            converted_action = (convert_to_user_input(other_action, 0), convert_to_user_input(action, 1))
        
        is_ball_touching_ground = self.engine.step(converted_action)
        self.engine.viewer.update()
        obs = self.engine.get_obs(self.pixel_mode)
        other_obs = self.engine.get_other_obs(self.pixel_mode)
        info = {
            'other_obs': other_obs
        }
        if is_ball_touching_ground:
            reward = -1 if self.engine.ball.punch_effect_x > GROUND_HALF_WIDTH else 1
            self.is_player2_serve = not (reward == -1)
            return obs, reward, True, True, info
        return obs, 0.0, False, False, info

    def reset(self, options=None, seed: Optional[int]=None, return_info: bool=False) -> Union[np.ndarray, Tuple[np.ndarray, dict]]:
        if seed is not None: self.engine.seed(seed)
        if options is None:
            self.engine.reset(self.is_player2_serve)
        elif 'is_player2_serve' in options:
            self.engine.reset(options['is_player2_serve'])
        else:
            raise KeyError
        obs = self.engine.get_obs(self.pixel_mode)
        other_obs = self.engine.get_other_obs(self.pixel_mode)
        info = {
            'other_obs': other_obs
        }
        return (obs, info)

    def close(self) -> None:
        self.engine.close()

class PikachuVolleyballPixelEnv(PikachuVolleyballEnv):
    pixel_mode = True
