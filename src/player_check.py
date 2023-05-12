import time
import json
import os

import schedule
import redis

from misc import configs
from misc.rcon import *

ROOT_PATH = configs.ROOT_PATH
DATA_PATH = configs.DATA_PATH

LOGGER    = configs.LOGGER
CONFIG    = configs.CONFIG
PORTS     = configs.PORTS

PASSWD    = CONFIG.passwd
HOST      = CONFIG.mrcon_host_ip
PORT      = PORTS.mrcon_port

RHOST     = CONFIG.global_host
RPORT     = PORTS.redis_port

LOGGER.info('[INFO.P-0001] 프로그램을 가동합니다.')
rcon  = RconInterface(HOST, PORT, PASSWD)
rconn = redis.Redis(host = RHOST, port = RPORT, 
                    db = 2, decode_responses = True) 

## 플레이어의 정보를 저장하는 함수.
def save_player_info():

    num_players = rcon.num_players()

    ## 접속해 있는 플레이어가 있는 경우
    if num_players != 0:
        players = rcon.online_players()

        print(players)
        for player in players:

            ## 플레이어 정보를 불러오는 함수
            player_info = rcon.who_is(player)

            time_interval = time.time() - player_info['latest_online']

            print(player_info)
            print(f'time interval : {time_interval:.2f}')

            ## 처음 데이터를 저장하거나 30분에 한 번씩 저장하도록 설정
            condition = [time_interval < 5, time_interval > 1800]
            if any(condition):
                
                LOGGER.info(f'[INFO.D-0001]{player}님의 데이터를 갱신합니다.')
                os.makedirs(f'{DATA_PATH}/json/', exist_ok = True)

                player_info['latest_online'] = time.time()
                with open(f'{DATA_PATH}/json/{player}.json', 'w') as f:
                    json.dump(player_info, f, indent = 2)

                rconn.set(player, json.dumps(player_info))
    
    ## 현재 접속해 있는 플레이어가 없는 경우
    else:
        LOGGER.info('[INFO.D-0002]현재 접속 중인 플레이어가 없습니다. 나중에 다시 요청바랍니다.')


schedule.every(30).seconds.do(save_player_info)
while True:

    schedule.run_pending()
    time.sleep(1)
