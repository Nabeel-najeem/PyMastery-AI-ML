#packages
import cv2
import numpy as np


def reorder(myPoints):
    # Reshape
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)] 
    myPointsNew[3] = myPoints[np.argmax(add)]
    
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)] 
    
    return myPointsNew

#Accesing web cam
cap = cv2.VideoCapture(0)

#size of detection
width, height = 480,640

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
    
    matrix = None
    
    imgout = np.zeros((height,width,3), dtype=np.uint8)
    
    
    #finding contours
    contour,_=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour :
        if cv2.contourArea(cnt) > 1000 :
            x,y,w,h = cv2.boundingRect(cnt)
            peri=0.02*cv2.arcLength(cnt,True)
            poly=cv2.approxPolyDP(cnt,peri,True)
            if len(poly) == 4 :
                cv2.drawContours(frame,[poly],-1,(0,255,255))
                pts1 = reorder(poly)
                pts1 = np.float32(pts1)
                pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
                matrix = cv2.getPerspectiveTransform(pts1,pts2)
    if matrix is not None :
        imgout = cv2.warpPerspective(frame,matrix,(width,height))
                
    
    
    
    #preview
    cv2.imshow("test",frame)
    cv2.imshow("warped",imgout)
    
    #key input
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    
    
    