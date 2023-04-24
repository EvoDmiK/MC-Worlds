from traceback import format_exc
import json
import time
import os
import re

from mcrcon import MCRcon as mrcon

from utils import logger, utils, configs

LOGGER    = logger.get_logger()
CONFIG    = configs.CONFIG
ROOT_PATH = CONFIG.ROOT_PATH
JSON_PATH = f'{ROOT_PATH}/MC-Worlds/src/logs/jsons'


class RCONInterface:

    def __init__(self, host, port, passwd):

        self.con = mrcon(host = host, port = port, password = passwd)
        
        try:
            self.con.connect()

        except Exception as e:

            LOGGER.error(f'서버에 연결할 수 없었습니다. 설정 값을 확인해 주세요.')
            LOGGER.error(format_exc())


    def _command(self, command):

        command = self.con.command(command)
        return re.sub('§[a-zA-Z0-9]', '', command).split('\n')


    def _only_digits(self, data):

        return re.sub('[^0-9]', ' ', data).split()[0]


    def _clear_minus(self, data):

        return [re.sub('[^a-zA-Z0-9]', '', data[0]), data[1].strip()]


    def num_players(self):

        players = self._command('list')
        players = [player for player in players if player != '']

        clear_data = lambda player: player.replace(' ', '').replace('[AFK]', '').split(':')[1].split(',')

        if num_players != 0:

            players = players[1: ]
            players = [clear_data(player) for player in players]

            return num_players, player

        else:
            LOGGER.info('현재 접속 중인 플레이어가 없습니다. 나중에 다시 요청 바랍니다.')
            return num_players


        