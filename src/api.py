from time import time
import json
import os

from fastapi import FastAPI

from misc import configs
from misc.rcon import *

ROOT_PATH = configs.ROOT_PATH
CONFIG    = configs.CONFIG 
PASSWD    = CONFIG.passwd
LOGGER    = loggers.get_logger()
HOST      = CONFIG.host
PORT      = CONFIG.port
rcon      = RconInterface
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

