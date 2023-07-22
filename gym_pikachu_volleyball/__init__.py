import os
from gymnasium import register
from gym_pikachu_volleyball.envs.pikachu_volleyball import PikachuVolleyballEnv

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

register(
        id="PikachuVolleyball-v0",
        entry_point='gym_pikachu_volleyball.envs:PikachuVolleyballEnv',
)
