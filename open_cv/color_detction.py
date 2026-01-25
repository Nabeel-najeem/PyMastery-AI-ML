import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

def empty():
    pass

cv2.namedWindow("hsv")
cv2.resizeWindow("hsv",640,240)
cv2.createTrackbar("HUE min","hsv",0,179,empty)
cv2.createTrackbar("HUE max","hsv",179,179,empty)
cv2.createTrackbar("sat min","hsv",0,255,empty)
cv2.createTrackbar("sat max","hsv",255,255,empty)
cv2.createTrackbar("value min","hsv",0,255,empty)
cv2.createTrackbar("value max","hsv",255,255,empty)


while True:
    _,frame=cap.read()
    #frame=cv2.flip(frame,1)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    h_min=cv2.getTrackbarPos("HUE min","hsv")
    h_max=cv2.getTrackbarPos("HUE max","hsv")
    s_min=cv2.getTrackbarPos("sat min","hsv")
    s_max=cv2.getTrackbarPos("sat max","hsv")
    v_min=cv2.getTrackbarPos("value min","hsv")
    v_max=cv2.getTrackbarPos("value max","hsv")
    
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    
    mask = cv2.inRange(hsv_frame,lower,upper)
    
    result = cv2.bitwise_and(frame,frame,mask=mask)
    
    hstack=np.hstack([result,frame])
    #hstack.resize(hstack,(960,360))
    
    
    cv2.imshow("hstack",hstack) 
    #cv2.imshow("result",result)
    
#    cv2.imshow("hexer",hsv_frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

    
   
    
    