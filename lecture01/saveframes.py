# saveframes.py
# read a video file and save every 100th frames

import numpy, cv2, sys

def saveFrames(video):
    stream = cv2.VideoCapture(video)
    numframe = 0
    while (stream.isOpened()):
        ret, frame = stream.read()
        if (ret == False): # finished all frames
            break
        # read a frame successful
        if ((numframe % 100) == 0):
            filename = 'frame' + str(numframe) + '.jpg'
            cv2.imwrite(filename, frame)
        numframe += 1
    print(numframe)
    stream.release()
            
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('need the name of a video file')
    saveFrames(sys.argv[1])
