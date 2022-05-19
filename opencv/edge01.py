# edge01.py
# detect edges in an image
# conver RGB image to gray
# detect sudden changes of intensity as edges
# save the gray image and the edge image

import numpy 
import sys
import cv2

def detectedge(filename, threshold):
    namebase = filename.replace('.JPEG', '')
    rgbimage = cv2.imread(filename)
    grayimage = cv2.cvtColor(rgbimage, cv2.COLOR_BGR2GRAY)
    grayname = namebase + '_gray.jpg'
    cv2.imwrite(grayname, grayimage)
    # print (grayimage.shape)
    [height, width] = grayimage.shape
    edgeimage = numpy.zeros([height, width])
    for row in range(1, height):
        for col in range(1, width):
            # print ([row, col])
            rowdiff = int(grayimage[row, col]) - int(grayimage[row - 1, col])
            rowdiff = abs(rowdiff)
            coldiff = int(grayimage[row, col]) - int(grayimage[row, col - 1])
            coldiff = abs(coldiff)
            if ((rowdiff > threshold) or (coldiff > threshold)):
                edgeimage[row, col] = 255
    edgename = namebase + '_edge' + str(threshold) + '.jpg'
    cv2.imwrite(edgename, edgeimage)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    thresholds = [1, 5, 10, 20, 40, 80, 160]
    for th in thresholds:
        detectedge(sys.argv[1], th)

