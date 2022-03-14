import cv2
import argparse
 
# Argument parsing variable declared
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",
                required=True,
                help="Path to folder")
ap.add_argument("-o", "--output",
                required=True,
                help="Path to folder")



args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
input_source = args["input"]
destination_folder = args["output"]


vidcap = cv2.VideoCapture(input_source)
success,image = vidcap.read()
count = 0



def get_zeros(count): 
    to_str = str(count)
    i = 6 - len(to_str)
    s = ""
    for i in range(0, i): 
        s += "0"
    return s 

while success:

    file_name = f"{destination_folder}/{get_zeros(count)}{count}.jpg"
    cv2.imwrite(file_name, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print(f'saved {file_name}...')
    count += 1


