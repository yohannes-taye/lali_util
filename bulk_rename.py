import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import os  
# Argument parsing variable declared
ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
ap.add_argument("-o", "--output",
                required=True, 
                help="Output folder path")

args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["image"]
outputpath = args["output"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
 
# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
 
    path = join(mypath, onlyfiles[n])
    file_extention = onlyfiles[n].split('.')[-1]
    new_name = join(mypath, f'{n}.{file_extention}')
    os.rename(path, new_name)
 
print("Files renamed successfully")