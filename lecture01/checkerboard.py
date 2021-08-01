# checkerboard.py
# create a checkerboard

import numpy, cv2
width = 400
eighth = int(width/8)

# create a 3-dimensional array
# first two dimensions for horizontal and vertical
# third dimension for colors (R, G, B)
# zeros make the pixels black
board = numpy.zeros([width, width, 3])

# create an 8 x 8 checkerboard

whitesquare = numpy.ones([eighth, eighth]) * 255

for row in range(8):
    for col in range(8):
        if ((row % 2) == (col % 2)):
            srow = row  * eighth    # start
            erow = srow + eighth    # end
            scol = col  * eighth
            ecol = scol + eighth
            board[srow:erow, scol:ecol, 0] = whitesquare
            board[srow:erow, scol:ecol, 1] = whitesquare
            board[srow:erow, scol:ecol, 2] = whitesquare

cv2.imwrite('checkerboard.jpg', board)
cv2.imshow('checkerboard', board)
cv2.waitKey(0)

