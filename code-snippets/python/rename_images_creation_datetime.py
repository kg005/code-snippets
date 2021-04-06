#!/usr/bin/env python3.6

# renames image files in given folder according to their creation date
# taken from
# https://orthallelous.wordpress.com/2015/04/19/extracting-date-and-time-from-images-with-python/

import os
from datetime import datetime as dt
from datetime import timedelta
from PIL import Image
import time

folder_path = 'C:/Users/karel.gavenciak/Desktop/Gruzie fotky Eva'


def imgDate(fn):
    "returns the image date from image (if available)\nfrom Orthallelous"
    std_fmt = '%Y:%m:%d %H:%M:%S.%f'
    # for subsecond prec, see doi.org/10.3189/2013JoG12J126 , sect. 2.2, 2.3
    tags = [(36867, 37521),  # (DateTimeOriginal, SubsecTimeOriginal)
            (36868, 37522),  # (DateTimeDigitized, SubsecTimeOriginal)
            (306, 37520), ]  # (DateTime, SubsecTime)
    exif = Image.open(fn)._getexif()

    for t in tags:
        dat_stmp = exif.get(t[0])
        sub_stmp = exif.get(t[1], 0)

        # PIL.PILLOW_VERSION >= 3.0 returns a tuple
        dat_stmp = dat_stmp[0] if type(dat_stmp) == tuple else dat_stmp
        sub_stmp = sub_stmp[0] if type(sub_stmp) == tuple else sub_stmp
        if dat_stmp != None: break

    if dat_stmp == None: return None
    full = '{}.{}'.format(dat_stmp, sub_stmp)
    # print(full)
    T = dt.strptime(full, std_fmt)
    # T = time.mktime(time.strptime(T, '%Y:%m:%d %H:%M:%S')) + float('0.%s' % sub)
    return T


for f in os.listdir(folder_path):
    date = imgDate(os.path.join(folder_path,f))

    os.rename(os.path.join(folder_path,f),os.path.join(folder_path,date.strftime('IMG_%Y%m%d_%H%M%S.JPG')))
    
