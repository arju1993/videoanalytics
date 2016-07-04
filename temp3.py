## Code for detecting Wheelchairs in an image.
## Prerequisites: dlib library git cloned from GitHub
##				  1. Cmake installed on the system
##				  2. The "imglab" executable file in the /dlib/tools/imgtools/build folder to be placed in the 
##				     folder containing images for test

## Editor : Vinod
## Last Edited on : 24 June 2016


## Import required packages
import os,sys
import glob
import dlib
from skimage import io
import numpy as np 
import time
import cv2


## Takes the user input for the folder path containing the images to be tested
input_path = raw_input('Enter path where images are to be placed:')
output_path = raw_input('Enter path to output folder:')
## Change the working directory to the path specified as input 
#os.chdir(input_path)
## Lines of code required to generate .xml file for the test images
#code = "./imglab -c testing.xml ./"
#os.system(code)

## This part of the code reads the video, converts it to frames, and currently considers every 10th frame to
## generate the .xml file. This has been done for testing purpose and can be modified to consider every frame or take an input from
## other models/codes
cap = cv2.VideoCapture('/home/musigma/Desktop/StoreFootage/StoreFootage.mp4')
ret = True
count = 0
while(ret):
	ret,frame = cap.read()
	count = count+1
	if ret==False:
		sys.exit()
	if count%10 == 0:
		filename = input_path + "/image_" + str(count) + '.jpg'
		cv2.imwrite(filename,frame)
		
		code = "./imglab -c testdataset.xml ./"
		os.system(code)
		testing_xml_path = os.path.join(input_path, "testdataset.xml")
		detector = dlib.simple_object_detector("store_footage.svm")
		#os.remove('/home/musigma/Desktop/Temp/testing.xml')
		os.remove("./testdataset.xml")
		
		#print("Showing detections on the images in the faces folder...")
		#win = dlib.image_window()
		for f in glob.glob(os.path.join(input_path, "*.jpg")):
			print("Processing file: {}".format(f))
			img = io.imread(f)
			dets = detector(img)
			#print("Number of faces detected: {}".format(len(dets)))
			for k, d in enumerate(dets):
				#print str(k) + "k"
				#print str(d) + "d"
			    #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
			     #   k, d.left(), d.top(), d.right(), d.bottom()))
				cv2.rectangle(img,(d.left(), d.top()),(d.right(), d.bottom()), (255,0,0),2)
		    	imagename = output_path + "/image_"+ str(count) + ".jpg"
		    	cv2.imwrite(imagename,img)
			     #os.remove(filename)
			     #print "found something"
	     	os.remove(filename)

			#win.clear_overlay()
        	#win.set_image(img)
        	#win.add_overlay(dets)

        	#filename = input_path + "/image_" + str(count) + '.jpg'
        	#cv2.imwrite(filename,frame)
        	#os.remove(filename)
        	#time.sleep(1)
