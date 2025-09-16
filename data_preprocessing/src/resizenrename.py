#!/usr/bin/python
from PIL import Image
import os, sys

path = "./train_dataset/synthetic/"
dirs = os.listdir( path )

def resize():
    count = 000
    for item in dirs:
        if os.path.isfile(path+item):
            im_1 = Image.open(path+item)
            im = im_1.convert('RGB')
            f, e = os.path.splitext(path+item)
            imResize = im.resize((512,512), Image.Resampling.LANCZOS)
            imResize.save('./train_dataset/synthetic_new/000'+ str(count) + '.jpg', 'JPEG', quality=100)
            count += 1

resize()