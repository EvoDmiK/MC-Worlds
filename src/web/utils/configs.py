import json

from easydict import EasyDict as edict

ROOT_PATH    = '/config/workspace/project'
_CONFIG_PATH = f'{ROOT_PATH}/utils/configs.json'
CONFIG       = json.loads(open(_CONFIG_PATH, 'r').read())
CONFIG       = edict(CONFIG) 