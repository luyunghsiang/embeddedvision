import cv2
import numpy
from matplotlib import pyplot as plot

### Load image to be segmented
### It will be a numpy array
imageToSegment = cv2.imread("arduino_uno_top.jpg")

### Apply a threshold to the image
### These values were determined by sampling the pixel values of the silkscreen
lowerBoundRGBValues = (210,210,210)
upperBoundRGBValues = (230,230,230)
postThresholdImage = cv2.inRange(imageToSegment, lowerBoundRGBValues, upperBoundRGBValues)

### Create kernel for dilation + erosion
kernel 	= numpy.ones( (7,7), numpy.uint8 )
dilated = cv2.dilate(postThresholdImage, kernel, iterations=1)
eroded 	= cv2.erode(dilated, kernel, iterations=1)

### Save the images
cv2.imwrite('dilated_eroded_thresold_img.png', eroded)
cv2.imwrite('dilated_threshold_img.png', dilated)
cv2.imwrite('thresold_img.png', postThresholdImage)

