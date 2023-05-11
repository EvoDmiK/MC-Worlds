## 내장 모듈
from traceback import format_exc
import json
import time
import os 
import re

## 써드파티 모듈
from mcrcon import MCRcon as mrcon
from redis import Redis

## 구현 모듈
from misc import configs

## 테스트 코드
# import configs, loggers

ROOT_PATH = configs.ROOT_PATH
DATA_PATH = configs.DATA_PATH

RHOST     = configs.CONFIG.global_host
RPORT     = configs.PORTS.redis_port
rconn     = Redis(host = RHOST, port = RPORT, 
                  db = 2, decode_responses = True)

class RconInterface:
    ## 클래스의 생성자
    def __init__(self, host: str, port: int, password: str):

        self.LOGGER = configs.LOGGER

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


    ## 현재 접속해 있는 플레이어 정보를 가져와주는 함수
    def _get_players(self) -> list:
        return [player for player in self._command('list') if player != '']


    ## 현재 접속 중인 플레이어 수와 닉네임을 불러와주는 함수
    def num_players(self) -> int:
        
        ## list 명령어를 통해서 서버에 들어와 있는 인원 수와 이름 정보 가져오기
        players     = self._get_players()
        num_players = players[0]
        num_players = int(self._only_digits(num_players)) 

        return num_players


    ## 플레이어 정보를 불러오는 함수
    def who_is(self, player : str) -> dict:

        infos = self._command(f'whois {player}')
        infos = [info for info in infos[1:] if info != '']
        infos = [self._clear_minus(info.split(':')) for info in infos]
        infos = {k : v for k, v in infos}

        try:
            ## 서버에 플레이어가 접속해 있지 않은 경우
            if infos == {}:
                json_path = f'{DATA_PATH}/json/{player}.json'
                
                ## redis에 존재하는 플레이어 정보 로딩
                try: infos  = json.loads(rconn.get(player))

                ## redis에 플레이어의 정보가 저장되어 있지 않은 경우
                ## 데이터 폴더에 저장되어 있는 플레이어 json 파일 로딩
                except:
                    self.LOGGER.error(f'[ERR.DB.Red.D-0001]현재 {player}의 정보가 저장되어 있는 파일이 존재하지 않습니다.')
                    infos = json.loads(open(json_path, 'r').read())

            ## 데이터를 처음 저장할때 마지막 로그인 시간을 현재로 저장하도록 설정
            infos['latest_online'] = infos['latest_online'] \
                                     if 'latest_online' in infos.keys() else time.time()

        except Exception as e:
            msg   = f'현재 {player}가 접속해 있지 않거나 {player}의 정보가 저장되어 있는 파일이 존재하지 않습니다.'
            infos = {'Nick' : msg}
            self.LOGGER.info(msg)
            self.LOGGER.error(e)

        return infos


    ## 현재 접속해 있는 플레이어들의 닉네임을 가져오는 함수
    def online_players(self) -> list:

        clear_name  = lambda player: player.replace(' ', '').replace('[AFK]', '').split(':')[1].split(',')
        players     = self._get_players()
        
        players = players[1:]
        players = [clear_name(player) for player in players]

        return players


if __name__ == '__main__':
    CONFIG      = configs.CONFIG
