import os

from imutils.paths import list_files
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from nbt import nbt
import numpy as np
import cv2

from misc.configs import *
from misc import constants


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




if __name__ == '__main__':

    data_paths = list_files(f'{DATA_PATH}/dat')
    MapGenerator.save_image(data_paths, n = 3)