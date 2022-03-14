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
                help="Output folder path")
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
for n in range(0, len(onlyfiles)):
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
    
    # Load the image in img variable
    img = cv2.imread(path, 1)
    old_image_height, old_image_width, channels = img.shape

    # create new image of desired size and color (blue) for padding
    new_image_width = int(width)
    new_image_height = int(height)
    color = (0,0,0)
    result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

    # compute center offset
    x_center = (new_image_width - old_image_width) // 2
    y_center = (new_image_height - old_image_height) // 2

    # copy img image into center of result image
    result[y_center:y_center+old_image_height, 
        x_center:x_center+old_image_width] = img

    # save result
    print(f"padded image {onlyfiles[n]}")
    cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', result)