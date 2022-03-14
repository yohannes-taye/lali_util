import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import numpy
from os.path import exists
import shutil

#depth should always be equal or less in number files compared to the destination
rgb_src = '/home/tmc/projects/LPTN/datasets/Lali/test/A'
depth_src = '/home/tmc/projects/LPTN/datasets/Lali/test/B'

rgb_dst = '/home/tmc/projects/LPTN/datasets/Lali/test/A_'
depth_dst = '/home/tmc/projects/LPTN/datasets/Lali/test/B_'



# Find all the images in the provided images folder

onlyfiles = [f for f in listdir(depth_src) if isfile(join(depth_src, f))]
images_in_folder1 = numpy.empty(len(onlyfiles), dtype=object)

for n in range(0, len(onlyfiles)):

    path = join(rgb_src, onlyfiles[n])
    depth_path = join(depth_src, onlyfiles[n])
    # img = cv2.imread(path, 1)
    if(exists(path)): 
        shutil.copy(path, rgb_dst)
        shutil.copy(depth_path, depth_dst)
    else: 
        print(f"Missing: {onlyfiles[n]} in {rgb_src}") 
    # print(f"Copying file {onlyfiles[n]}")
    # cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', crop)
 
print("Files copied successfuly")