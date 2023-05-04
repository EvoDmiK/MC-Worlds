from time import time
import json
import os

from fastapi import FastAPI

from misc import configs, logger
from misc.rcon import *

ROOT_PATH = configs.ROOT_PATH
CONFIG    = configs.CONFIG
PASSWD    = CONFIG.passwd
HOST      = CONFIG.mrcon_host_ip

PORTS     = configs.PORTS
PORT      = PORTS.mrcon_port

LOGGER    = logger.get_logger()
app       = FastAPI()


LOGGER.info('API 서버를 기동합니다.')
rcon = RconInterface(HOST, PORT, PASSWD)

@app.post('/')
def root(): return {'Hello' : 'Welcome'}


@app.post('/num_players/')
async def num_players():

    num_players = rcon.num_players()
    return json.dumps({'num_players' : num_players})


@app.post('/who_is/')
async def who_is(player: str):
    
    player_info = rcon.who_is(player)
    return json.dumps(player_info)

