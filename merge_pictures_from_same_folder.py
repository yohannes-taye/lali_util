import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import debugpy
from tqdm import tqdm
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


 
ap.add_argument("-i", "--img",
                required=True,
                help="Path to folder for the first image directory")

ap.add_argument("-s", "--separator", 
               required=True, 
               help="Separtor used to tell the two files appart (eg. _original)")

ap.add_argument("-o", "--out",
                required=True, 
                help="Output folder path for the final merged result")
        
 
args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["img"]
outputpath = args["out"]
separator = args["separator"]

create_dir(outputpath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = sorted(onlyfiles)

images = numpy.empty(len(onlyfiles), dtype=object)
 

for n in tqdm(range(0, len(onlyfiles))):
 
    path = join(mypath, onlyfiles[n])
    path2 = join(mypath, onlyfiles[n].split('.')[0] + separator + '.' + onlyfiles[n].split('.')[1])
    if os.path.isfile(path) and os.path.isfile(path2):
        img1 = cv2.imread(path)
        img2 = cv2.imread(path2)
        numpy_horizontal = np.hstack((img1, img2))
        cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', numpy_horizontal)

    

print("Images merged Successfully")