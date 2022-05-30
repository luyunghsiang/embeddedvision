# read an image and show it
import cv2
import sys
def showImage(filename):
    img = cv2.imread(filename)
    cv2.imshow("imshow", img)
    k = cv2.waitKey(0)
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    showImage(sys.argv[1])

    
