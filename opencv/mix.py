# read two images and show the mixed image
import cv2 
import sys
def mixImage(filename1, filename2):
    img1 = cv2.imread(filename1)
    img2 = cv2.imread(filename2)
    # only images of the same size can be added
    size1 = img1.shape
    size2 = img2.shape
    height = min(size1[0], size2[0])
    width  = min(size1[1], size2[1])
    print (size1)
    print (size2)
    print ([height, width])
    nimg1 = cv2.resize(img1, [width, height])
    nimg2 = cv2.resize(img2, [width, height])
    img3 = cv2.addWeighted(nimg1, 0.5, nimg2, 0.5, 0)
    cv2.imshow('imshow', img3)
    cv2.imwrite('mixed.jpg', img3)
    k = cv2.waitKey(0)
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        sys.exit('need the name of two image files')
    mixImage(sys.argv[1], sys.argv[2])

    
