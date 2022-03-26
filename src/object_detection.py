# Author: Artan Zandian
# December 2021

import jetson.inference
import jetson.utils

# load the object detection model with 91 classes trained on COCO classes
# The threshold identifies tht amount of detection
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# Setting up camera
# for list of available cameras on command line run $ v4l2-ctl --list-devices
camera = jetson.utils.videoSource('/dev/video0')

# Display loop
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
	img = camera.Capture()
	# do detection on the captured video frame (img)	
	detections = net.Detect(img)
	# render to display
	display.Render(img)
	
