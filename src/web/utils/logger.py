import logging

def get_logger():

    logger = logging.getLogger('DoveWeb')
    logger.setLevel(logging.INFO)

    formatter      = logging.Formatter('[%(asctime)s][%(levelname)s] %(name)s : %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':

    logger = get_logger()
    logger.info('로깅 스타트') 