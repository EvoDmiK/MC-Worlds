from traceback import format_exc
import json
import os

from easydict import EasyDict as edict

from misc import logger
# import logger

ROOT_PATH          = '/config/workspace/project'
DATA_PATH          = f'{ROOT_PATH}/MC-Worlds/src/data'
CONFIG_PATH        = f'{ROOT_PATH}/utils/configs'
CONFIG_BACKUP_PATH = f'{ROOT_PATH}/BACKUPS/configs'
LOGGER             = logger.get_logger()

## json 파일을 불러와주는 함수
load_json     = lambda json_path: json.loads(open(json_path, 'r').read())

## json 파일을 저장하는 함수
save_json     = lambda data, json_path: json.dump(data, open(json_path, 'w'), indent = 2)

def repair_json(json_path, ftype = 'config'):

    try: json_ = load_json(f'{json_path}/{ftype}.json')
    except Exception as e:

        LOGGER.error(f'[ERR.K.A-0001] json 파일이 깨져 열 수 없습니다. {e} \n{format_exc()}')
        texts = open(f'{CONFIG_BACKUP_PATH}/{ftype}.txt', 'r').readlines()
        texts = [text.split() for text in texts]
        json_ = {name : text for name, text in texts}

        save_paths = [CONFIG_PATH, CONFIG_BACKUP_PATH]
        for save_path in save_paths:

            os.makedirs(save_path, exist_ok = True)
            save_json(json_, f'{save_path}/{ftype}.json')

    finally: return json_


def get_json(ftype = 'config'):

    if os.path.isfile(f'{CONFIG_PATH}/{ftype}.json'):
        config = repair_json(CONFIG_PATH, ftype = ftype)

    else:
        LOGGER.warning('[WARN.K.A-0001] json 파일이 존재하지 않아 백업 데이터를 로딩합니다.')
        config = repair_json(CONFIG_BACKUP_PATH, ftype = ftype)

    return edict(config)


CONFIG = get_json()
PORTS  = get_json(ftype='ports')
