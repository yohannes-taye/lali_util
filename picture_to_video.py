import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import glob
from tqdm import tqdm

ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
ap.add_argument("-o", "--output",
                required=True, 
                help="Output folder path")
# ap.add_argument("-d", "--dimention", 
#                 required=True, 
#                 help="width/height")
ap.add_argument("-f", "--fps", 
                required=True, 
                help="FPS")



args = vars(ap.parse_args())    

mypath = args["image"]
outputpath = args["output"]
fps = int(args["fps"])
# width, height = args["dimention"].split("/")
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# # fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
# # video = cv2.VideoWriter('{outputpath}/video.avi', fourcc, 1, (width, height))
# frame_array = []
# frame_size = (int(width), int(height))
# output = cv2.VideoWriter(f'{outputpath}/video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 1, 20, frame_size, True)
# for n in tqdm(range(0, len(onlyfiles)), desc="Processing"):
#     path = join(mypath, onlyfiles[n])
#     img = cv2.imread(join(mypath, onlyfiles[n]),
#                            cv2.IMREAD_UNCHANGED)
#     output.write(img)
# output.release()
 
def create_avi(): 
    img_array = []
    size = None 
    for filename in tqdm(sorted(glob.glob(f'{mypath}/*jpg')), desc="Reading Frames"):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    out = cv2.VideoWriter(f'{outputpath}/video.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in tqdm(range(len(img_array)), desc="Creating video"):
        out.write(img_array[i])
    out.release()



img_array = []
size = None 
for filename in tqdm(sorted(glob.glob(f'{mypath}/*jpg')), desc="Reading Frames"):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter(f'{outputpath}/video.mp4',cv2.VideoWriter_fourcc(*'MP4V'), fps, size)
for i in tqdm(range(len(img_array)), desc="Creating video"):
    out.write(img_array[i])
out.release()
