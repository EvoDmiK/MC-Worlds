from traceback import format_exc
from collections import Counter
from datetime import datetime
import math as math
import time
import json
import os
import re

from imutils.paths import list_files
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import pymysql as sql
from nbt import nbt
import numpy as np
import cv2

from misc.configs import *
from misc import constants

ROOT_PATH = ROOT_PATH
LOGGER    = LOGGER
CONFIG    = CONFIG
PORTS     = PORTS


unix2datetime = lambda unixtime: str(datetime.fromtimestamp(unixtime)).split(':')[:-1]

load_json     = lambda json_path: json.loads(open(json_path, 'r').read())

save_json     = lambda data, json_path: json.dump(data, open(json_path, 'w'))


class MapGenerator:

    def read_data(data_path):

        file = nbt.NBTFile(data_path)
        return file['data']


    def gencolors(allcolors, basecolors, alphacolor):

        allcolors           = []
        basecolors[0]       = alphacolor
        allcolorsinversemap = {}

        
        for odx, basecolor in enumerate(basecolors):

            r = round
            if odx == 0:

                allcolors.extend([alphacolor] * 4)
                allcolorsinversemap[alphacolor] = 3

            else:
                for idx in range(4):
                    m = (180, 220, 255, 135)[idx]

                    new_color = (r(basecolor[0] * m / 255), r(basecolor[1] * m / 255), r(basecolor[2] * m / 255))
                    allcolors.append(new_color)
                    allcolorsinversemap[new_color] = odx * 4 + idx

        return allcolors * 2


    def save_image(data_paths, n = 1):

        for idx, data_path in enumerate(data_paths, 1):
            
            if 'map' not in data_path: continue
            os.makedirs(f'{DATA_PATH}/map', exist_ok = True)

            color_data = MapGenerator.read_data(data_path)['colors'].value
            image      = Image.new('RGB', (128, 128))
            draw       = ImageDraw.Draw(image)

            alphacolor = constants.alphacolor
            basecolors = constants.basecolors 
            allcolors  = constants.allcolors

            allcolors  = MapGenerator.gencolors(allcolors, basecolors, alphacolor)
            map_data   = [allcolors[v] for v in color_data]

            file_name  = f'{DATA_PATH}/map/map_{str(idx).zfill(3)}.jpg'
            image.putdata(map_data)
            image = image.resize((128 * n, 128 * n), Image.LANCZOS)
            image.save(file_name, 'JPEG', quality = 100, subsampling = 0)


class DataBase:

    def __init__(self, db_name):

        self.db_name = db_name
        self.passwd  = CONFIG.sql_passwd
        self.host    = CONFIG.global_host
        self.user    = CONFIG.sql_user
        self.port    = PORTS.sql_port

        self.connect_db()

    
    def connect_db(self):

        self.conn   = sql.connect(host = self.host, port = self.port,
                                user = self.user, passwd = self.passwd, db = self.db_name)

        self.cursor = self.conn.cursor()


    def search_table(self, table_name, columns = '*', platform = 'steam', **kwargs):

        sorting_col = kwargs['sorting_col'] if 'sorting_col' in kwargs else columns
        sorting_col = sorting_col if sorting_col != '*' else \
                      ('appid' if type(sorting_col) != list else sorting_col[0])

        conditions  = kwargs['conditions'] if 'condition' in kwargs else None
        how_many    = kwargs['how_many']   if 'how_many'  in kwargs else 1
        reverse     = kwargs['desc']       if 'desc'      in kwargs else False

        col_indexes = {k : v for v, k in enumerate(['idx', 'appid', 'name', 'percent', 
                                                    'original', 'discounted', 'date'])}

        ## 코드가 너무 킹받게 짜졌다..
        col_indexes = col_indexes if columns == '*' else \
                    ({k : v for v, k in enumerate(columns)} \
                    if type(columns) == list else {columns : 0})

        col_keys = [col for col in col_indexes.keys()]
        
        try:
            
            assert sorting_col in col_keys, f'''\n[ERR.DB.Co-0001] 선택하신 조건에 맞는 컬럼이 존재하지 않아 선택 하신 옵션으로 정렬 할 수 없었습니다. \
                                                {col_keys}에서 골라 주십시오.'''

            columns = ', '.join(columns) if type(columns) == list else columns

            print(f'\n\n {columns} \n\n')
            ## 데이터 조회할 때 그 어떤 조건도 없는 경우 그냥 테이블에서 컬럼만 받아 사용
            if conditions == None:
                query = f"""
                            SELECT DISTINCT {columns} FROM {table_name} WHERE platform='{platform}'
                        """
            
            else:
                ## 고급 쿼리에 사용할 거
                conditions = np.array(conditions)

                ## WHERE 문으로 찾을 column, 조건, 데이터를 받아 조회해준다.
                if len(conditions) == 3:
                    col, cond, data = conditions

                    print('\n\n', col, cond, data, '\n\n')
                    symbols = ['>', '<', '!=', '=', '>=', '<=', 'IN']
                    assert cond in symbols, f'\n[ERR.DB.Co-0002] 조건이 올바르지 않습니다. {symbols}에서 선택해 넣어주십시오.'
            
                    
                    query = f"""
                                SELECT DISTINCT {columns} FROM {table_name}
                                WHERE {col} {cond} {data} AND platform='{platform}';
                            """
                
                ## 데이터를 찾을 column과 찾을 data만 있는 경우
                ## 기본값으로 동일한 데이터만 찾도록 지정해주었다.
                elif len(conditions) == 2:
                    col, data = conditions
                    query = f"""
                                SELECT DISTINCT {columns} FROM {table_name}
                                WHERE {col}={data} AND platform='{platform}';
                            """

            self.cursor.execute(query)
            
            ## 데이터 정렬에 사용할 인덱스 값들.
            col_index = col_indexes[sorting_col]

        except Exception as e:
            LOGGER.error(f'[ERR.DB.Q-0001] 쿼리에 문제가 발생하였습니다. 확인 후 수정 바랍니다. \n{format_exc()}')
            query     = f'SELECT * FROM {table_name}'
            col_index = 0

        ## how_many가 0을 포함한 음의 정수가 된다면 모든 데이터를 조회해준다.
        return sorted(self.cursor.fetchmany(how_many), 
                      key = lambda x: x[col_index], reverse = reverse)



if __name__ == '__main__':

    data_paths = list_files(f'{DATA_PATH}/dat')
    MapGenerator.save_image(data_paths, n = 3)