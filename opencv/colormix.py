# colormix.py
# create three overlapping areas of RGB
import math
import numpy, cv2
width = 400
third = int(width/3)

def drawCircle(crow, ccol, radius, canvas, color):
    # draw a filled cirlce center at (crow, ccol)
    for row in range(radius):
        col = int(math.sqrt(radius * radius - row * row))
        canvas[crow - row: crow + row, ccol - col: ccol + col, color] = 255

canvas = numpy.zeros([width, width, 3])
drawCircle(third, third, third, canvas, 0)
drawCircle(2 * third, third, third, canvas, 1)
drawCircle(int(width / 2), 2 * third, third, canvas, 2)
cv2.imwrite('colormix.jpg', canvas)

