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


 
ap.add_argument("-i1", "--img1",
                required=True,
                help="Path to folder for the first image directory")
                 
ap.add_argument("-i2", "--img2",
                required=True,
                help="Path to folder for second image directory ")
ap.add_argument("-o", "--out",
                required=True, 
                help="Output folder path for the final merged result")
 
args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["img1"]
secondpath = args["img2"]
outputpath = args["out"]
create_dir(outputpath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = sorted(onlyfiles)
onlyfiles2 = [f for f in listdir(secondpath) if isfile(join(secondpath, f))]
onlyfiles2 = sorted(onlyfiles2)
images = numpy.empty(len(onlyfiles), dtype=object)
 
# Iterate through every image
# and resize all the images.

# debugpy.listen(5678)
# print("Press play!")
# debugpy.wait_for_client()


for n in tqdm(range(0, len(onlyfiles))):
 
    path = join(mypath, onlyfiles[n])
    img1 = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)

    img2 = cv2.imread(join(secondpath, onlyfiles2[n]))
    numpy_horizontal = np.hstack((img1, img2))
    # numpy_horizontal = np.hstack((img2, cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)))
    
    cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', numpy_horizontal)

print("Images resized Successfully")