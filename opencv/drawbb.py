# draw bounding boxes and labels
import cv2
import sys

def readshow(imgfile, bbfile):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
              (255, 0, 255), (0, 255, 255), (255, 255, 255)] 
    img = cv2.imread(imgfile)
    height, width, color = img.shape
    print (height, width, color)
    fhd = open(bbfile, 'r')
    lastlabel = ''
    clr = colors[0]
    labelcnt = 0
    for line in fhd:
        [xm, ym, xM, yM, conf, name] = line.split(',')
        name = name.strip() # remove ending '\n'
        xmin = int(xm)
        ymin = int(ym)
        xmax = int(xM)
        ymax = int(yM)
        print (xmin, ymin, xmax, ymax, conf, name)
        # check whether this is valid
        if ((xmin > xmax) or (ymin > ymax)):
            print('Error 1')
        if ((xmax > width) or (ymax > height)):
            print('Error 2')
            print(xmax, width, ymax, height)
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), clr, 2)
        cv2.putText(img, name, (xmin, ymin), 2, 1, clr)
        labelcnt = (labelcnt + 1) % (len(colors))
        clr = colors[labelcnt]
    img2name = imgfile.replace('.jpg', 'bb.jpg')
    cv2.imwrite(img2name, img)
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        sys.exit('two files')
    readshow(sys.argv[1], sys.argv[2])
