import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
 
# Argument parsing variable declared
ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
ap.add_argument("-o", "--output",
        required=True, 
        help="Output f  older path")

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
    # Load the image in img variable
    img = cv2.imread(path, 1)
    print(f"Generating data {onlyfiles[n]}")
    filename = onlyfiles[n].split('.')[0] + '.jpg'
    cv2.imwrite(f'{outputpath}/{filename}', img)
 
print("Data generated Successfully")