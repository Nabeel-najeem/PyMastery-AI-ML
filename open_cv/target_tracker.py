import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    succes,frame=cap.read()
    
    imgblur=cv2.GaussianBlur(frame,(7,7),3)
    gray_frame=cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    
    
    cv2.imshow("test",gray_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    