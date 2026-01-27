import cv2
import numpy as np

cap=cv2.VideoCapture(0)

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
    
    coutours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in coutours:
        
        if cv2.contourArea(cnt)>1000:
            m=cv2.moments(cnt)
            x,y,w,h=cv2.boundingRect(cnt)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    
    if m["m00"]!=0:
        cx=int(m["m10"]/m["m00"])
        cy=int(m["m01"]/m["m00"])
    
    
    
    
    cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.circle(result,(cx,cy),5,(0,0,255),2)
    result=cv2.flip(result,1)
    
    cv2.putText(result,f"x = {x} / y = {y}",(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    
    
    
    
    cv2.imshow("hstack",result) 
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

    