import os
import numpy as np
import cv2 as cv

people=[]
for i in os.listdir(r'D:\Open CV\train photos'):
    people.append(i)
 
dir=r"D:\Open CV\train photos"
hara_caascade= cv.CascadeClassifier("hara_face.xml")

features=[]
labels=[]


def create_train():
    for person in people:
        path= os.path.join(dir,person)
        label=people.index(person)

        for image in os.listdir(path):
            ima_path=os.path.join(path,image)
            img_array = cv.imread(ima_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect=hara_caascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print("length of the features:", len(features))
print("length of the labels:",len(labels))
print("training part is done..............")
features=np.array(features,dtype='object')
labels=np.array(labels)
  
#crating the face recogniser 
face_recognizer = cv.face.LBPHFaceRecognizer_create()
#training the recognizer on the features list and the labels list 
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
