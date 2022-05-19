# swapredblue.py
# swap the values of red and blue of each pixel

import numpy, cv2, sys
import matplotlib.pyplot as pyplot

def swapredblue(image):
    dimension = image.shape
    for row in range(dimension[0]):
        for col in range(dimension[1]):
            # read the original values
            blue = image[row, col, 0]
            red  = image[row, col, 2]
            # swap
            image[row, col, 0] = red
            image[row, col, 2] = blue
            
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    image = cv2.imread(sys.argv[1])
    swapredblue(image)
    cv2.imwrite('swappedimage.jpg', image)
