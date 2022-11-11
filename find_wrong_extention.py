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

args = vars(ap.parse_args())
 
mypath = args["image"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
 
# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
    file_extention = onlyfiles[n].split('.')[-1]
    if file_extention != "JPG":
        print(onlyfiles[n])
 
print("Done!")