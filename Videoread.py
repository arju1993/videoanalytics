import cv2
import math
import numpy as np


#################### Setting up the file ################
videoFile = "/home/musigma/Desktop/StoreFootage.mp4"
vidcap = cv2.VideoCapture(videoFile)
success,image = vidcap.read()

#################### Setting up parameters ################

seconds = 10
fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

#################### Initiate Process ################

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()

    if frameId % multiplier == 0:
        cv2.imwrite("/home/musigma/Desktop/StoreFootage/frame%d.jpg" % frameId, image)

vidcap.release()
print "Complete"
