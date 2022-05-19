# colorhistogram.py
# draw the histograms or Red, Green, Blue

import numpy, cv2, sys
import matplotlib.pyplot as pyplot

def histogram(image):
    dimension = image.shape
    intensity = numpy.zeros([256, 3])
    for row in range(dimension[0]):
        for col in range(dimension[1]):
            for clr in range(3):
                intensity[image[row, col, clr], clr] += 1
    # plot the three colors
    xaxis = range(256)
    yaxis = range(256)
    # print(len(intensity[:,0]))
    pyplot.scatter(xaxis, intensity[:,0], color = 'b', marker = 'o')
    pyplot.scatter(xaxis, intensity[:,1], color = 'g', marker = '+')
    pyplot.scatter(xaxis, intensity[:,2], color = 'r', marker = 'x')
    pyplot.savefig('colorhistogram.jpg')

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of an image file')
    image = cv2.imread(sys.argv[1])
    histogram(image)


    
