import os,sys
import glob
import dlib
from skimage import io
import time

 #./imglab -c mydataset.xml /tmp/images

## Takes the path of the folder containing test images and the imglab executable file
## and generates a XML for the set of test images in the folder

input_path = raw_input('Enter path where images are placed:')
os.chdir(input_path)


code = "./imglab -c testing.xml ./"
os.system(code)

## Confirm that the XML file is generated

if os.path.isfile("./testing.xml"):
	confirm = "XML file has been generated"
	print "XML file has been generated"
else:
	confirm = "Not created"
	print "Not created"

if confirm == "Not created":
	sys.exit()
else:
	testing_xml_path = os.path.join(input_path, "testing.xml")
	print("Testing accuracy: {}".format(dlib.test_simple_object_detector(testing_xml_path, "detector.svm")))
	detector = dlib.simple_object_detector("detector.svm")
	win_det = dlib.image_window()
	win_det.set_image(detector)

	print("Showing detections on the images in the faces folder...")
	win = dlib.image_window()
	for f in glob.glob(os.path.join(input_path, "*.jpg")):
	    print("Processing file: {}".format(f))
	    img = io.imread(f)
	    dets = detector(img)
	    print("Number of faces detected: {}".format(len(dets)))
	    for k, d in enumerate(dets):
	        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
	            k, d.left(), d.top(), d.right(), d.bottom()))
	     
		win.clear_overlay()
		win.set_image(img)
		win.add_overlay(dets)
		#save_png(img,"detected.png")
		#dlib.hit_enter_to_continue()
		time.sleep(10)
