## 내장 모듈
from traceback import format_exc
import json
import time
import os 
import re

## 써드파티 모듈
from mcrcon import MCRcon as mrcon

## 구현 모듈
from misc import configs, loggers

ROOT_PATH   = '/config/workspace'
CONFIG      = configs.CONFIG
LOGGER      = loggers.logger

class RconInterface:

    def __init__(self, host, port, password, name = None):

        ## RCON 서버에 접속해 주는 부분 (이게 되야 모든 코드가 돌아감,, 흑흑)
        self.con = mrcon(host = host, port = port, password = password)
        try: self.con.connect()

        except Exception as e:
            LOGGER.error(f'서버에 연결 할 수 없었습니다. 설정값을 확인해주세요.')
            LOGGER.error(format_exc())

    
    ## RCON에 명령어 전달해주는 함수
    def command(self, command):

        command = self.con.command(command)

        ## 커맨드를 입력해 결과를 받아오면 §c, §6처럼 붙어있는게 있어서
        ## 정규표현식으로 제거해주고, \n을 기준으로 나눠서 배열에 저장

        ## e.g.) 현재 접속 중인 인원은 §c0/§620명 입니다.\ndefault§f:§sJohnDoe\n
        ##       => ['현재 접속 중인 인원은 0/20명 입니다.', 'default : JohnDoe', '']
        return re.sub('§[a-zA-Z0-9]', '', command).split('\n')


    def only_digits(self, data):

        ## 파라미터로 전달 받은 값에서 숫자만 추출한 값에서 첫 번째 값만 사용
        ## e.g) '현재 접속 중인 인원은 0/20명 입니다.' => ['0', '20'] => '0'
        return re.sub('[^0-9]', ' ', data).split()[0]


    ## 현재 접속 중인 플레이어 수와 닉네임을 불러와주는 함수
    def num_players(self):
        
        ## list 명령어를 통해서 서버에 들어와 있는 인원 수와 이름 정보 가져오기
        players = self.command('list')
        players = [player for player in players if player != '']

        num_players = players[0]
        num_players  = int(self.only_digits(num_players)) 

        ## 누군가 서버에 들어와 있는 경우
        if num_players != 0:
            players = players[1:]
            players = [player.replace(' ', '').split(':')[1] for player in players]

            return num_players, players

        ## 서버에 아무도 없는 경우
        else:
            LOGGER.info('현재 접속 중인 플레이어가 없습니다. 나중에 다시 요청바랍니다.')
            return num_players


    ## 현재 접속 중인 플레이어 정보를 가져오는 함수
    def who_is(self):

        try:
            _, players = self.num_players()
            
            
            for player in players:
                player_info = self.command(f'whois {player}')

                for infos in player_info:
                    
                    infos = [info for info in infos if info != '']
                    infos = infos.replace(' ', '').split(':')


        except:
            LOGGER.info('현재 접속 중인 플레이어가 없습니다. 나중에 다시 요청바랍니다.')
            LOGGER.info(format_exc())


if __name__ == '__main__':

    start_time = time.time()
    mrcon = RconInterface(CONFIG.host, CONFIG.port, CONFIG.passwd)
    mrcon.who_is()
    print(time.time() - start_time)