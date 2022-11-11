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

ap.add_argument("-w", "--width", 
                required=True, 
                help="Width")
ap.add_argument("-c", "--height", 
                required=True, 
                help="Height")

args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["image"]
outputpath = args["output"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
 
def pad_image(img):
    print(img.shape)
    current_height, current_width, l = img.shape

    desired_width = int(args["width"])
    desired_height = int(args["height"])
    right_padding = np.zeros((current_height, desired_width - current_width, l))
    img = np.hstack((img, right_padding))
    bottom_padding = np.zeros((desired_height - current_height, img.shape[1] , l))
    img = np.vstack((img, bottom_padding))
    return img
for n in range(0, len(onlyfiles)):
 
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
 
    print(f"padding image {onlyfiles[n]}")
    
    img = cv2.imread(path, 1)
    img = pad_image(img)
    # Save the image in Output Folder
    cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', img)

print("Images padded Successfully")