import cv2
cap=cv2.VideoCapture(0)
while True:
    succes,frame=cap.read()
    if not succes:
        break
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #print(f"Camera resolution: {width} x {height}")
    
    cv2.circle(frame,(640,310),20, (0,255,0),thickness=10)
    cv2.circle(frame,(640,310),5, (0,0,255),thickness=5)
    cv2.putText(frame,"pupil tracking",(1000,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    cv2.imshow("hexer service",frame)
    
    if cv2.waitKey(1)&0xFF==ord('q'): 
        break