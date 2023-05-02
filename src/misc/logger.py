from datetime import date
import logging
import os

def get_logger():

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

    ## 로그 포매터와 파일 핸들러 logger에 설정
    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info('server start!!')

