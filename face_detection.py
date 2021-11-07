#Face detection using hara cascading 
import cv2 as cv
import numpy as np
#rescalling 
def rescaling(frame,scale=0.40):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimentions=(width,height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)
#----------------------------------
img = cv.imread('group2.jpg')
rescaled_img= rescaling(img)
cv.imshow("rescaled img",rescaled_img)
#cv.imshow("lady",img)
gray=cv.cvtColor(rescaled_img,cv.COLOR_BGR2GRAY)
cv.imshow("grey image",gray)
hara_caascade= cv.CascadeClassifier("hara_face.xml")

faces_rect = hara_caascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print("number of faces found =",len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(rescaled_img,(x,y),(x+w,y+h),(0,255,0),thickness=2) 
cv.imshow("ditected faces ",rescaled_img)
cv.waitKey(0) & 0xff==ord("q")
