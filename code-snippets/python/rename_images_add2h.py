#!/usr/bin/env python3.6
# add 2 hours to images filenames
import os
from datetime import datetime as dt
from datetime import timedelta
from PIL import Image
import time


folder_path = 'C:/Users/karel.gavenciak/Desktop/Gruzie fotky Eva'


for f in os.listdir(folder_path):
    date = dt.strptime(f,'IMG_%Y%m%d_%H%M%S.JPG')

    os.rename(os.path.join(folder_path,f),os.path.join(folder_path,(date + timedelta(hours=2)).strftime('IMG_%Y%m%d_%H%M%S.JPG')))