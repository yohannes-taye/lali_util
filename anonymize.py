import cv2
import argparse
from tqdm import tqdm
from os import listdir
from os.path import isfile, join





ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
 
ap.add_argument("-o", "--output",
                required=True, 
                help="Output folder path")

args = vars(ap.parse_args())
 
mypath = args["image"]
outputpath = args["output"]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# to detect the face of the human
cascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# a while loop to run infinite times,
# to capture infinite number of frames for video
# because a video is a combination of frames
for n in range(0, len(onlyfiles)):
    frame = cv2.imread(
        join(mypath, onlyfiles[n]), 
        cv2.IMREAD_UNCHANGED)

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(
		gray_image, scaleFactor=2.0, minNeighbors=4)

    for x, y, w, h in face:

		# draw a border around the detected face.
		# (here border color = green, and thickness = 3)
        image = cv2.rectangle(frame, (x, y), (x+w, y+h),
							(0, 255, 0), 3)

		# blur the face which is in the rectangle
        image[y:y+h, x:x+w] = cv2.medianBlur(image[y:y+h, x:x+w],
											35)

	# show the blurred face in the video
    cv2.imwrite(f'{outputpath}/{onlyfiles[n]}', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print("Done!")