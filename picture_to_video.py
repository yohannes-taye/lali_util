import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy

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

mypath = args["image"]
outputpath = args["output"]
width, height = args["dimention"].split("/")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
# video = cv2.VideoWriter('{outputpath}/video.avi', fourcc, 1, (width, height))
frame_array = []
frame_size = (width, height)
output = cv2.VideoWriter('{outputpath}/video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 1, 20, frame_size, True)
for n in range(0, len(onlyfiles)):
    path = join(mypath, onlyfiles[n])
    img = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
    output.write(img)
    # video.write(img)
    # frame_array.append(img)
    # height, width, layers = img.shape 
    # size = (width, height)

# video = cv2.VideoWriter('{outputpath}/video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 25, size)
# for i in range(len(frame_array)): 

output.release()