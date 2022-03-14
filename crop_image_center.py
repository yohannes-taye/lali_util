import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import debugpy
# Argument parsing variable declared
ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
ap.add_argument("-o", "--output",
                required=True, 
                help="Output f  older path")
ap.add_argument("-d", "--dimention", 
                required=True, 
                help="width/height")

args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["image"]
outputpath = args["output"]
width, height = args["dimention"].split("/")

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
 

# debugpy.listen(5678)
# print("press play")
# debugpy.wait_for_client()

# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
 
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
 
    # Load the image in img variable
    img = cv2.imread(path, 1)
    original_height, original_width, _ = img.shape
    padding_width = int((original_width - int(width)) / 2) 
    padding_height = int((original_height - int(height)) / 2)
    print(f"Padding width: {padding_width}")
    print(f"Padding height: {padding_height}")
    crop = img[padding_height:padding_height+int(height), padding_width:padding_width+int(width)]
    # Define a resizing Scale
    # To declare how much to resize
    # Save the image in Output Folder
    print(f"cropping image {onlyfiles[n]}")
    cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', crop)

 
print("Images resized Successfully")