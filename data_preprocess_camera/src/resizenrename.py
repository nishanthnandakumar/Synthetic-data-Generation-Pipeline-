#!/usr/bin/python
from PIL import Image
import os, sys
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Process two input paths.')
parser.add_argument('--path_a', type=str, required=True, help='Path to input images')
parser.add_argument('--path_b', type=str, required=True, help='Path to output images')

args = parser.parse_args()

# Use the path
input_path = args.path_a
output_path = args.path_b

dirs = os.listdir( input_path )

def resize():
    count = 000
    for item in dirs:
        if os.path.isfile(input_path+item):
            im_1 = Image.open(input_path+item)
            im = im_1.convert('RGB')
            f, e = os.path.splitext(input_path+item)
            imResize = im.resize((960,250), Image.Resampling.LANCZOS)
            imResize.save(str(output_path) + '000'+ str(count) + '.jpg', 'JPEG', quality=100)
            count += 1

resize()