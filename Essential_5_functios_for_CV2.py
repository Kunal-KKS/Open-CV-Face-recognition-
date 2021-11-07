import cv2 as cv
import numpy as np
img= cv.imread("im1.jpg")
cv.imshow("Innitial Image",img)
#grayscaling the image 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray Image",gray)
#how to blur an image using open cv
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

#cascading the edges of the image 
canny=cv.Canny(img,125,200)
cv.imshow("cascaded edges",canny)

#dilating the image
dilate=cv.dilate(canny,(5,5),iterations=3)
cv.imshow("dilated image",dilate)

#eroding the image (reversing the dilation process)
erode= cv.erode(dilate,(3,3),iterations=3)
cv.imshow("eroded Image",erode)




cv.waitKey(0) & 0xff==ord("q")
