import numpy as np
import os 
import cv2 as cv 
people=[]
for i in os.listdir(r'D:\Open CV\train photos'):
    people.append(i)
 
hara_caascade= cv.CascadeClassifier("hara_face.xml")
#features= np.load("features.npy")
#labels=np.load("labels.npy")
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread("T5.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray image",gray)

faces_rect=hara_caascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    face_roi= gray[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(face_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')
    cv.putText(img,str(people[label]), (20,50),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow("Detected Face",img)
cv.waitKey(0)
