# 1]Face recognition on image

import cv2
import sys

#load the cascade
face_cascade=cv2.CascadeClassifier(r'C:\Users\omkar desai\OneDrive\Desktop\Artificial Inteligence\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
#read thre input image
img=cv2.imread(r'C:\Users\omkar desai\OneDrive\Desktop\Artificial Inteligence\friends.jpg')
img
#convert into multiscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray
#detect faces
faces=face_cascade.detectMultiScale(gray,1.1,3)#(gray factor,scaling vales,neighbour points)
faces
f=len(faces)
f
#DRAW RECTANGLE AROUNG FACES
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"face",(x,y),font,1,(255,0,0))
    #cv2.putText(img,f,(x,y),font,1,(255,0,0))
    

#display the output
cv2.imshow('img',img)
cv2.waitKey(0)
#-------------------------------------------------------------------------------------------------------------------------------
# 2]Face recognition on video

import sys
import cv2

#load the cascade
face_cascade=cv2.CascadeClassifier(r'C:\Users\omkar desai\OneDrive\Desktop\Artificial Inteligence\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
#read the input video
a=cv2.VideoCapture(r'C:\Users\omkar desai\OneDrive\Desktop\Artificial Inteligence\Smiling.mp4')
print(a)
while True:
    b,c=a.read()
    if(b==True and c is not None):
        c=cv2.resize(c,(500,500))
        #convert into multiscale
        gray=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
        #detect faces
        faces=face_cascade.detectMultiScale(gray,1.1,5)#(gray factor,scaling vales,neighbour points)

        #DRAW RECTANGLE AROUNG FACES
        for (x,y,w,h) in faces:
            cv2.rectangle(c,(x,y),(x+w,y+h),(225,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(c,"face",(x,y),font,2,(0,0,225))
        
        cv2.imshow('video',c)
        if ord('q')==cv2.waitKey(20):
            cv2.destroyAllWindows()
            break
    else:
        break

cv2.destroyAllWindows()
a.release()

#-------------------------------------------------------------------------------------------------------------------------------
# 1]Face recognition on live camera

import sys
import cv2

#load the cascade
face_cascade=cv2.CascadeClassifier(r'C:\Users\omkar desai\OneDrive\Desktop\Artificial Inteligence\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
#read the input video
a=cv2.VideoCapture(0)
print(a)
while True:
    b,c=a.read()
    if(b==True and c is not None):
        c=cv2.resize(c,(1000,1000))
        #convert into multiscale
        gray=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
        #detect faces
        faces=face_cascade.detectMultiScale(gray,1.2,8)#(gray factor,scaling vales,neighbour points)

        #DRAW RECTANGLE AROUNG FACES
        for (x,y,w,h) in faces:
            cv2.rectangle(c,(x,y),(x+w,y+h),(225,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(c,"face",(x,y),font,2,(0,0,225))
        
        cv2.imshow('video',c)
        if ord('q')==cv2.waitKey(20):
            cv2.destroyAllWindows()
            break
    else:
        break

cv2.destroyAllWindows()
a.release()
