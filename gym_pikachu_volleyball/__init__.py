import os
from gymnasium import register
from gym_pikachu_volleyball.envs.pikachu_volleyball import PikachuVolleyballEnv, PikachuVolleyballPixelEnv, PikachuVolleyballRandomEnv

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

register(
        id="PikachuVolleyball-v0",
        entry_point='gym_pikachu_volleyball.envs:PikachuVolleyballEnv',
)

register(
        id="PikachuVolleyballPixel-v0",
        entry_point='gym_pikachu_volleyball.envs:PikachuVolleyballPixelEnv',
)

register(
        id="PikachuVolleyballRandom-v0",
        entry_point='gym_pikachu_volleyball.envs:PikachuVolleyballRandomEnv',
)