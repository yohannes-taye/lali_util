import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import os  



def create_dir(d):
    """ Create a directory if it does not exist
    Args:
        d: directory to create
    """
    if not os.path.exists(d):
        os.makedirs(d)


# Argument parsing variable declared
ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
ap.add_argument("-o", "--output",
                required=True, 
                help="Output folder path")
ap.add_argument("-d", "--dim", 
                required=True, 
                help="widthxheight")

args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["image"]
outputpath = args["output"]
height, width  = args["dim"].split("x")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
 
# Iterate through every image
# and resize all the images.\
create_dir(outputpath)
for n in range(0, len(onlyfiles)):
 
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
 
    # Load the image in img variable
    img = cv2.imread(path, 1)
 
    # Define a resizing Scale
    # To declare how much to resize
    resized_dimensions = (int(height), int(width))
 
    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions,
                               interpolation=cv2.INTER_AREA)
 
    # Save the image in Output Folder
    print(f"resizing image {onlyfiles[n]}")
    cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', resized_image)

 
print("Images resized Successfully")


