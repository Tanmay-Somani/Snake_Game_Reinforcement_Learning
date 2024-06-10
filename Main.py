import gym_super_mario_bros as gim
from SuperMarioBros_actions import RIGHT_ONLY
from nes_py.wrappers import JoypadSpace


ENV_name="SuperMarioBros-1-1-v3"
env=gim.make(ENV_name,render_mode='human',apply_api_compatibility=True)
env=JoypadSpace(env,RIGHT_ONLY)

done=False
env.reset()