## 내장 모듈
from traceback import format_exc
import json
import time
import os 
import re

## 써드파티 모듈
from mcrcon import MCRcon as mrcon

## 구현 모듈
from misc import configs, logger

## 테스트 코드
# import configs, loggers

ROOT_PATH = configs.ROOT_PATH
SAVE_PATH = configs.DATA_PATH

class RconInterface:

    def __init__(self, host, port, password):

        self.LOGGER = logger.get_logger()

        ## RCON 서버에 접속해 주는 부분 (이게 되야 모든 코드가 돌아감,, 흑흑)
        self.con    = mrcon(host = host, port = port, password = password)

        try: self.con.connect()

        except Exception as e:
            self.LOGGER.error(f'서버에 연결 할 수 없었습니다. 설정값을 확인해주세요.')
            self.LOGGER.error(format_exc())

    ## RCON에 명령어 전달해주는 함수
    def _command(self, command: str) -> str:

        command = self.con.command(command)

        ## 커맨드를 입력해 결과를 받아오면 §c, §6처럼 붙어있는게 있어서
        ## 정규표현식으로 제거해주고, \n을 기준으로 나눠서 배열에 저장

        ## e.g.) 현재 접속 중인 인원은 §c0/§620명 입니다.\ndefault§f:§sJohnDoe\n
        ##       => ['현재 접속 중인 인원은 0/20명 입니다.', 'default : JohnDoe', '']
        return re.sub('§[a-zA-Z0-9]', '', command).split('\n')


    ## 데이터에서 숫자만 추출해주는 함수
    def _only_digits(self, data: str) -> list:

        ## 파라미터로 전달 받은 값에서 숫자만 추출한 값에서 첫 번째 값만 사용
        ## e.g) '현재 접속 중인 인원은 0/20명 입니다.' => ['0', '20'] => '0'
        return re.sub('[^0-9]', ' ', data).split()[0]


    ## 플레이어 정보를 가져왔을 때 2차원 배열에서 
    ## 첫 번째 원소는 알파벳, 숫자만 추출하고, 두 번째 원소는 공백을 지워주는 함수
    def _clear_minus(self, data : list) -> list:

        ## e.g.) ['- Nick', ' DoveKim'] -> ['Nick', 'DoveKim']
        return [re.sub('[^a-zA-Z0-9]', '', data[0]), data[1].strip()]


    ## 현재 접속 중인 플레이어 수와 닉네임을 불러와주는 함수
    def num_players(self) -> int:
        
        ## list 명령어를 통해서 서버에 들어와 있는 인원 수와 이름 정보 가져오기
        players = self._command('list')
        players = [player for player in players if player != '']

        num_players = players[0]
        num_players  = int(self._only_digits(num_players)) 

        clear_data = lambda player: player.replace(' ', '').replace('[AFK]', '').split(':')[1].split(',')

        ## 누군가 서버에 들어와 있는 경우
        if num_players != 0:
            players = players[1:]
            players = [clear_data(player) for player in players]

            return num_players, players

        ## 서버에 아무도 없는 경우
        else:
            self.LOGGER.info('현재 접속 중인 플레이어가 없습니다. 나중에 다시 요청바랍니다.')
            return num_players


    ## 플레이어 정보를 불러오는 함수
    def who_is(self, player : str) -> dict:

        infos = self._command(f'whois {player}')
        infos = [info for info in infos[1:] if info != '']
        infos = [self._clear_minus(info.split(':')) for info in infos]
        infos = {k : v for k, v in infos}

        try:
            infos = infos if infos != {} else json.loads(open(f'{SAVE_PATH}/{player}.json', 'r').read())

        except:
            msg   = f'현재 {player}가 접속해 있지 않거나 {player}의 정보가 저장되어 있는 파일이 존재 하지 않습니다.'
            infos = {'Nick' : msg}
            self.LOGGER.error(msg)

        return infos


    
    ## 플레이어 정보를 저장하는 함수
    def save_info(self):

        try:
            _, players = self.num_players()
            
            for player in players:
                player_info = self.who_is(player)

                os.makedirs(SAVE_PATH, exist_ok = True)
                with open(f'{SAVE_PATH}/{player}.json', 'w') as f:
                    json.dump(player_info, f, indent = 2)

        except:
            self.LOGGER.info('현재 접속 중인 플레이어가 없습니다. 나중에 다시 요청바랍니다.')
            self.LOGGER.info(format_exc())



if __name__ == '__main__':
    CONFIG      = configs.CONFIG
