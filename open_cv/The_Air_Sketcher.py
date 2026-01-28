import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def empty():
    pass


cv2.namedWindow("hsv control")
cv2.resizeWindow("hsv control",640,240)

cv2.createTrackbar("HUE min","hsv control",0,179,empty)
cv2.createTrackbar("HUE max","hsv control",179,179,empty)
cv2.createTrackbar("sat min","hsv control",0,255,empty)
cv2.createTrackbar("sat max","hsv control",255,255,empty)
cv2.createTrackbar("value min","hsv control",0,255,empty)
cv2.createTrackbar("value max","hsv control",255,255,empty)

canvas = None
px , py = 0,0

brush = False



while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    
    h_min=cv2.getTrackbarPos("HUE min","hsv control")
    h_max=cv2.getTrackbarPos("HUE max","hsv control")
    s_min=cv2.getTrackbarPos("sat min","hsv control")
    s_max=cv2.getTrackbarPos("sat max","hsv control")
    v_min=cv2.getTrackbarPos("value min","hsv control")
    v_max=cv2.getTrackbarPos("value max","hsv control")
    
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    
    mask=cv2.inRange(hsv_frame,lower,upper)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        if cv2.contourArea(cnt)>1000:
            m=cv2.moments(cnt)
            x,y,w,h=cv2.boundingRect(cnt)    
            
    if m["m00"]!=0:
        cx=int(m["m10"]/m["m00"])
        cy=int(m["m01"]/m["m00"])
        
    if canvas is None:
        canvas=np.zeros_like(frame)
        
    if px == 0 and py ==0 :
        px, py, = cx, cy
        
    if brush :
        cv2.line(canvas,(px, py), (cx, cy),(0,200,0), 2)
    
    

    px, py = cx ,cy
    cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.circle(result,(cx,cy),5,(0,255,200),10)
    
    #canvas=cv2.bitwise_or(result,canvas,mask=mask)
    final_result=cv2.addWeighted(frame,1,canvas,1,0)
    
    
    
    cv2.imshow("result",final_result)
    cv2.imshow("feed",result)
    

    
    
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
    elif key == ord('b'):
        brush= not brush
    elif key == ord('c'):
        canvas=np.zeros_like(frame)


