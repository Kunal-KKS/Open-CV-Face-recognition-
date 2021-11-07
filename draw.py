import cv2 as cv
import numpy as np
blank= np.zeros((500,500,3), dtype='uint8')

#img = cv.imread("im1.jpg")
cv.imshow("dog",blank)
#painting on the image 
blank[:]=0,255,0
cv.rectangle(blank, (0,0),(250,250), (255,0,0) , thickness=3)
cv.imshow("Green",blank)
cv.rectangle(blank, (250,0),(500,250), (255,0,0) , thickness=3)
cv.circle(blank,(250,250),50,(0,0,200),thickness=-1)
cv.line(blank,(0,0),(250,250),(0,0,0),thickness=2)
cv.imshow("circle", blank)
cv.waitKey(0)
