# segmentation01.py
# an image using the mean shift method

import numpy 
import sys
import cv2

def detectedge(filename):
    namebase = filename.replace('.JPEG', '')
    image = cv2.imread(filename)
    shifted = cv2.pyrMeanShiftFiltering(image, 5, 9)
    '''
    (21, 51) is used on
    https://www.pyimagesearch.com/2015/11/02/watershed-opencv/
    no explanation why these values are used
    '''
    cv2.imshow('mean shift', shifted)
    shiftedname = namebase + '_meanshift59.jpg'
    cv2.imwrite(shiftedname, shifted)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    detectedge(sys.argv[1])

