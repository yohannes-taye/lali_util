import numpy as np
import cv2 as cv
import glob
import random 
import argparse


################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################
ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
    required=True,
    help="Path to folder")

ap.add_argument("-s", "--samples",
    required=True,
    help="How many frames to sample inside folder")

ap.add_argument("-c", "--checker",
    required=True,
    help="Checker board width and height")

ap.add_argument("-o", "--out", 
    required=True, 
    help="Output file for camera intrinsic")

args = vars(ap.parse_args())

mypath = args["image"]
samples = int(args["samples"])
checker_board_shape = args["checker"].split(",")
outpath = args["out"]


chessboardSize = (int(checker_board_shape[0]), int(checker_board_shape[1]))
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)
size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


images = glob.glob(f'{mypath}/*.jpg')
images = random.sample(images, samples)
frameSize = None 
# print(images)

for image in images:

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    frameSize = img.shape
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
    print(f"Processing: {image}")
    # If found, add object points, image points (after refining them)
    if ret == True:
        print("Chessboard detected..")
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        # cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        # cv.imshow('img', img)
        # cv.wai/home/tmc/Documents/Data/lali_phone_calibration_matrix/img/selectedALIBRATION #######################################################

ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
print(cameraMatrix)
a_file = open(f"{outpath}/camera_intrinsic.txt", "w")
np.savetxt(a_file, cameraMatrix)

############## UNDISTORTION #####################################################

# img = cv.imread('cali5.png')
# h,  w = img.shape[:2]
# newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))



# # Undistort
# dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('caliResult1.png', dst)



# # Undistort with Remapping
# mapx, mapy = cv.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w,h), 5)
# dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('caliResult2.png', dst)




# # Reprojection Error
# mean_error = 0

# for i in range(len(objpoints)):
#     imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
#     error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
#     mean_error += error

# print( "total error: {}".format(mean_error/len(objpoints)) )