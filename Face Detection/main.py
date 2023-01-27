import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
_,frame = cap.read()
frame = cv2.resize(frame,(640,480))
roi = cv2.selectROI(frame)

while True:
    _ ,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    im_cropped = frame[int(roi[1]):int(roi[1]+roi[3]),
    int(roi[0]): int(roi[0]+roi[2])]
    gray = cv2.cvtColor(im_cropped ,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05 ,minNeighbors = 4, minSize = (30,30))
    for x,y,w,h in faces:
        cv2.rectangle(im_cropped,(x,y),(x+w, y+h),(0,255,0),2)
    cv2.imshow('Face ID',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
