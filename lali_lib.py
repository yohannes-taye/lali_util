

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import glob
from tqdm import tqdm


def frame_to_video(images_folder, output_folder, file_name, fps): 
    print("Converting to video..")
    img_array = []
    size = None 
    pngs = glob.glob(f'{images_folder}/*png')
    jpgs = glob.glob(f'{images_folder}/*jpg')
    for filename in tqdm(sorted(pngs + jpgs), desc="Reading Frames"):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter(f'{output_folder}/{file_name}.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in tqdm(range(len(img_array)), desc="Creating video"):
        out.write(img_array[i])
    out.release()
    print(f"Video saved at {output_folder}/{file_name}.avi")


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

 
