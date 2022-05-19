# edge03.py
# detect edges in an image using the Canny detector

import numpy 
import sys
import cv2

def detectedge(filename):
    namebase = filename.replace('.JPEG', '')
    image = cv2.imread(filename)
    edges = cv2.Canny(image, 100, 200)
    edgename = namebase + '_canny.jpg'
    cv2.imwrite(edgename, edges)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    detectedge(sys.argv[1])

