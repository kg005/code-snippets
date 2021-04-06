#!/usr/bin/env python3.6

# rename exif creation date for each image in given folder according to their creation date + 2h
# taken from
# https://stackoverflow.com/questions/44636152/how-to-modify-exif-data-in-python

import os
from datetime import datetime as dt
from datetime import timedelta
from PIL import Image
import time
import piexif

folder_path = 'C:/Users/karel.gavenciak/Desktop/Gruzie fotky Eva - spravne datum nazev'


def imgDate(fn):
    "returns the image date from image (if available)\nfrom Orthallelous"
    std_fmt = '%Y:%m:%d %H:%M:%S.%f'
    # for subsecond prec, see doi.org/10.3189/2013JoG12J126 , sect. 2.2, 2.3
    tags = [36867,  # (DateTimeOriginal, SubsecTimeOriginal)
            36868,]  # (DateTimeDigitized, SubsecTimeOriginal)
            # (306, 37520), ]  # (DateTime, SubsecTime)
    img = Image.open(fn)
    exif_dict = piexif.load(img.info['exif'])

    for t in tags:
        dat_stmp = str(exif_dict['Exif'][t],encoding='utf-8')

        # PIL.PILLOW_VERSION >= 3.0 returns a tuple
        dat_stmp = dat_stmp[0] if type(dat_stmp) == tuple else dat_stmp

        datetime_obj = dt.strptime(dat_stmp, '%Y:%m:%d %H:%M:%S')
        datetime_obj += timedelta(hours=2)

        exif_dict['Exif'][t] = datetime_obj.strftime('%Y:%m:%d %H:%M:%S').encode('utf-8')

    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, fn)
    print('done', fn)


for f in os.listdir(folder_path):
    imgDate(os.path.join(folder_path,f))



