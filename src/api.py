from time import time
import json
import os

from fastapi import FastAPI

from misc import configs, loggers
from misc.rcon import *

ROOT_PATH = configs.ROOT_PATH
CONFIG    = configs.CONFIG 
LOGGER    = loggers.logger
PASSWD    = CONFIG.PASSWD
HOST      = CONFIG.HOST
PORT      = CONFIG.PORT
rcon      = RconInterface
app       = FastAPI()

LOGGER.info('API 서버 기동을 시작합니다.')
rcon = RconInterface(HOST, PORT, PASSWD)

@app.post('/')
def root(): return {'Hello' : 'Welcome'}


@app.post('/num_players/')
async def num_players():

    try:

