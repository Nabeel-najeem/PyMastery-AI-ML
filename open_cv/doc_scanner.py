#packages
import cv2
import numpy as np

#Accesing web cam
cap = cv2.VideoCapture(0)

#loop for video process and continue read
while True :
    succes,frame = cap.read()
    frame= cv2.flip(frame,1)
    
    #preview
    cv2.imshow("test",frame)
    
    
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    
    
    