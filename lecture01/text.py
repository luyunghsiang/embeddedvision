# text.py
# add text to an image

import numpy 
import sys
import cv2

def addText(filename):
    rgbimage = cv2.imread(filename)
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 255, 0) # green
    textimage = cv2.putText(rgbimage, 'OpenCV', (100, 100), font, 1, color)
    cv2.imwrite("text.jpg", textimage)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    addText(sys.argv[1])

