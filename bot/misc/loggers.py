from datetime import date
import logging
import os

from misc import configs

ROOT_PATH = configs.ROOT_PATH
LOG_PATH  = f'{ROOT_PATH}/project/MC-Worlds/bot/logs'

today     = date.today().strftime('%Y-%m-%d')

## INFO 이상의 로그만 출력
logger  = logging.getLogger('DoveCraft')
logger.setLevel(logging.INFO)

## 로그 출력문의 포맷을 지정하는 핸들러 설정
## asctime   : 로그가 찍힌 시간
## name      : getLogger의 파라미터로 입력한 이름
## levelname : 로그의 위험도 (ERROR/  DEBUG / INFO / WARNING)
## message   : 로그 메시지

formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

os.makedirs(LOG_PATH, exist_ok = True)

try:
    today_logs = [file for file in os.listdir('logs') if today in file]
    idx        = str(len(today_logs)).zfill(3)

except: idx = '000'

## 로그 파일 저장해주는 핸들러 지정
file_handler = logging.FileHandler(f'{LOG_PATH}/{today}_{idx}.log')

## 로그 포매터와 파일 핸들러 logger에 설정
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logger.info('server start!!')

