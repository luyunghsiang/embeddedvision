# frame2video.py
# create a video from individual frames of images
# a bouncing white ball

import numpy 
import math
from cv2 import VideoWriter, VideoWriter_fourcc

width = 1280
height = 720
FPS = 24
seconds = 10
radius = int(height/8)

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./ball.avi', fourcc, float(FPS), (width, height))
square = numpy.ones((int(height/4), int(width/4), 3), dtype=numpy.uint8) * 255

# create a white ball
ball = numpy.zeros((2 * radius, 2 * radius, 3), dtype=numpy.uint8)
for row in range(radius):
    col = int(math.sqrt(radius * radius - row * row))
    ball[radius - row: radius + row, radius - col: radius + col, ] = 255
deltarow = int(3 * height / (FPS * seconds))    
srow = radius

for count in range(FPS*seconds):
    canvas = numpy.zeros((height, width, 3), dtype = numpy.uint8)
    scol = int (count * 3 * width / (4 * FPS * seconds))
    canvas[srow - radius: srow + radius, scol: scol + 2 * radius,] = ball
    srow += deltarow

    # change direction?
    if ((srow + deltarow) < radius):
        deltarow = - deltarow
    if ((srow + deltarow) >= (height - radius)):
        deltarow = - deltarow
    
    video.write(canvas)
video.release()
