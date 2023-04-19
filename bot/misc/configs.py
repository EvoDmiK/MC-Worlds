import json

from easydict import EasyDict as edict

ROOT_PATH   = '/config/workspace'
CONFIG_PATH = f'{ROOT_PATH}/utils/configs.json'
CONFIG      = json.loads(open(CONFIG_PATH, 'r').read())
CONFIG      = edict(CONFIG)