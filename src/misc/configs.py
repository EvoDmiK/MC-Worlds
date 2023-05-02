from traceback import format_exc
import json
import os

from easydict import EasyDict as edict

from misc import logger

ROOT_PATH        = '/config/workspace/project'
DATA_PATH        = f'{ROOT_PATH}/MC-Worlds/src/data/jsons'
JSON_PATH        = f'{ROOT_PATH}/utils/'
JSON_BACKUP_PATH = f'{ROOT_PATH}/BACKUPS/configs'

CONFIG_NAMES     = [   'port',   'host',  'passwd', 'api_host',
                    'youtube',  'steam', 'openai',
                    'mrcon_api_int_port',
                    'mrcon_api_ext_port',
                    'chimhaha_int_port', 
                    'chimwiki_int_port', 
                    'dovenest_int_port', 
                    'dovenest_api_int_port']

LOGGER       = logger.get_logger()

## json 파일을 불러와주는 함수
load_json     = lambda json_path: json.loads(open(json_path, 'r').read())

## json 파일을 저장하는 함수
save_json     = lambda data, json_path: json.dump(data, open(json_path, 'w'))

def repair_config(json_path):

    try: config = load_json(f'{json_path}/config.json')

    except Exception as e:

        LOGGER.error(f'json 파일이 깨져 열 수 없습니다. {e} \n{format_exc()}')
        texts = open(f'{JSON_BACKUP_PATH}/config.txt', 'r').read().split('\n')

        texts  = [text.split() for text in texts]
        texts  = [text for text in texts if text != []]

        config = {name : text for name, text in texts}
        save_paths = [JSON_PATH, JSON_BACKUP_PATH]
        for save_path in save_paths:

            os.makedirs(save_path, exist_ok = True)
            save_json(config, f'{save_path}/config.json')

    
    finally: return config

def get_config():

    if os.path.isfile(f'{JSON_PATH}/config.json'):
        config = repair_config(JSON_PATH)

    else:
        LOGGER.warning('json 파일이 존재하지 않아 백업 데이터를 로딩합니다.')
        config = repair_config(JSON_BACKUP_PATH)

    return edict(config)

CONFIG = get_config()
