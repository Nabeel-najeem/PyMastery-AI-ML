#packages
import cv2
import numpy as np

#Accesing web cam
cap = cv2.VideoCapture(0)

#loop for video process and continue read
while True :
    #frame capturing
    succes,frame = cap.read()
    #mirror the video
    frame= cv2.flip(frame,1)
    #convert the color to gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #gausion blur
    blur=cv2.GaussianBlur(gray,(3,3),0)
    #finding edges
    edges=cv2.Canny(blur,100,200)
    #kernal
    kernal = np.ones((5,5))
    #cleaning pipe line
    dial = cv2.dilate(edges,kernal,iterations=2)
    threshold = cv2.erode(dial,kernal,iterations=1)
    
    
    #finding contours
    contour,_=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour :
        if cv2.contourArea(cnt) > 1000 :
            x,y,w,h = cv2.boundingRect(cnt)
            peri=0.02*cv2.arcLength(cnt,True)
            poly=cv2.approxPolyDP(cnt,peri,True)
            if len(poly) == 4 :
                cv2.drawContours(frame,[poly],-1,(0,255,255))
                
    
    
    
    #preview
    cv2.imshow("test",frame)
    
    #key input
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    
    
    