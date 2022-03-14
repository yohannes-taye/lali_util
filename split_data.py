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
ap.add_argument("--o1",
                required=True, 
                help="Output folder path for folder A")

ap.add_argument("--o2",
                required=True, 
                help="Output folder path for folder B")

 

args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["image"]
output_path_a = args["o1"]
output_path_b = args["o2"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
bin_container = [] 
# Iterate through every image
# and resize all the images.

for n in range(0, len(onlyfiles)):
    bin_container.append(onlyfiles[n])
    file_id = int(onlyfiles[n].split('.')[0])
    path = join(mypath, onlyfiles[n])
    img = cv2.imread(path, 1)
    
    if(file_id % 2 != 0):
        cv2.imwrite(f'{output_path_a}/{onlyfiles[n]}', img)
    else:
        cv2.imwrite(f'{output_path_b}/{onlyfiles[n]}', img)  
    print(f"Generating data {onlyfiles[n]}")
 
print("Data Split Successfully")