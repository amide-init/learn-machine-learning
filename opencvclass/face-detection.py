import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade =  cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    i = 0
    for (x, y, w, h) in faces:
        i += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0),2)
        cv2.putText(frame,'face'+str(i) , (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        rof_gray = gray[y:y+h, x:x+w]
        rof_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(rof_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(rof_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()