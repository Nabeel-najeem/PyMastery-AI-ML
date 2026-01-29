#packages
import cv2
import numpy as np

# web cam assecing
cap=cv2.VideoCapture(0)

# empty function 
def empty():
    pass

# task bar creation
cv2.namedWindow("hsv control")
cv2.resizeWindow("hsv control",640,240)
cv2.createTrackbar("HUE min","hsv control",0,179,empty)
cv2.createTrackbar("HUE max","hsv control",179,179,empty)
cv2.createTrackbar("sat min","hsv control",0,255,empty)
cv2.createTrackbar("sat max","hsv control",255,255,empty)
cv2.createTrackbar("value min","hsv control",0,255,empty)
cv2.createTrackbar("value max","hsv control",255,255,empty)

#empty balck screen creation 
canvas = None
px , py = 0,0

# current brush status
brush = False
# brsh color
drawn_color = (100,100,100)
#brush size
brush_size=2

#kernal for noise reduction
kernal = np.ones((5,5),np.uint8)



# loop for live feed and proceesings
while True:
    
    #frame reading
    _,frame=cap.read()
    
    #frame mirror
    flip_frame=cv2.flip(frame,1)
    
    #add gausion blur
    frame=cv2.GaussianBlur(flip_frame,(3,3),0)
    
    #color conertion to hsv
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #geting track values
    h_min=cv2.getTrackbarPos("HUE min","hsv control")
    h_max=cv2.getTrackbarPos("HUE max","hsv control")
    s_min=cv2.getTrackbarPos("sat min","hsv control")
    s_max=cv2.getTrackbarPos("sat max","hsv control")
    v_min=cv2.getTrackbarPos("value min","hsv control")
    v_max=cv2.getTrackbarPos("value max","hsv control")
    
    #create the lower higher variable for masking
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    
    #creating mask 
    mask=cv2.inRange(hsv_frame,lower,upper)
    
    # noise reduction 
    
    mask = cv2.erode(mask,kernal,iterations= 1)
    
    mask = cv2.dilate(mask,kernal,iterations=2)
    
    
    
    
    #creating feed for selecting color
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    # finding area
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    # finding countors and moments for centroid 
    for cnt in contours:
        if cv2.contourArea(cnt)>1000:
            m=cv2.moments(cnt)
            x,y,w,h=cv2.boundingRect(cnt)    
    
    # find the center of object     
    if m["m00"]!=0:
        cx=int(m["m10"]/m["m00"])
        cy=int(m["m01"]/m["m00"])
    
    #crash saftey   
    if canvas is None:
        canvas=np.zeros_like(frame)
    #for drawing smooth with past and prestent  
    if px == 0 and py ==0 :
        px, py, = cx, cy
    #pause the play for brsh   
    if brush :
        cv2.line(canvas,(px, py), (cx, cy),drawn_color, brush_size)
    
    
    #drawings on feed
    px, py = cx ,cy
    cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.circle(result,(cx,cy),5,(0,255,200),10)
    
    #craeting final output for aircanvas with overlying drawings 
    final_result=cv2.addWeighted(frame,1,canvas,1,0)
    
    
    #ui overlay for colour change 
    #   RED
    cv2.rectangle(final_result,(50,10),(150,60),(0,0,255),cv2.FILLED)
    cv2.putText(final_result,"RED",(70,45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
    cv2.rectangle(final_result,(160,10),(260,60),(0,255,255),cv2.FILLED)
    cv2.putText(final_result,"yellow",(165,45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
    cv2.rectangle(final_result,(270,10),(370,60),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"White",(275,45),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.rectangle(final_result,(380,10),(530,60),(0,0,0),cv2.FILLED)
    cv2.putText(final_result,"Erraser",(400,45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
    # drawn color chnaging
    if 50 < cx < 150 and 10 < cy < 60 :
        drawn_color= (0,0,255)
        brush_size=2
    elif 160 < cx < 260 and 10 < cy < 60 :
        drawn_color = (0,255,255)
        brush_size=2
    elif 270 < cx < 370 and 10 < cy < 60 :
        drawn_color = (255,255,255)
        brush_size=2
    #erraser
    elif 380 < cx < 530 and 10 < cy < 60 :
        drawn_color = (0,0,0)
        brush_size=50
        
    # Brsh size ui
    
    cv2.rectangle(final_result,(1190,10),(1240,60),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"2",(1205,45),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.rectangle(final_result,(1190,70),(1240,120),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"4",(1205,105),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.rectangle(final_result,(1190,130),(1240,180),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"6",(1205,165),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.rectangle(final_result,(1190,190),(1240,240),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"8",(1205,225),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.rectangle(final_result,(1190,250),(1240,300),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"10",(1190,285),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.rectangle(final_result,(1190,310),(1240,360),(255,255,255),cv2.FILLED)
    cv2.putText(final_result,"12",(1190,345),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    #brush size change 
    if 1190 < cx < 1240 and 10 < cy < 60 :
        brush_size=2
    elif 1190 < cx < 1240 and 70 < cy < 120 :
        brush_size=4
    elif 1190 < cx < 1240 and 130 < cy < 180 :
        brush_size=6
    elif 1190 < cx < 1240 and 190 < cy < 240 :
        brush_size=8
    elif 1190 < cx < 1240 and 250 < cy < 300 :
        brush_size=10
    elif 1190 < cx < 1240 and 310 < cy < 360 :
        brush_size=12

        
    #for shoow airbrush window and colour selecting window
    cv2.imshow("result",final_result)
    cv2.imshow("feed",result)
    cv2.imshow("test",flip_frame)
    
    
    #keys for quit,brush and clean
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
    elif key == ord('b'):
        brush= not brush
    elif key == ord('c'):
        canvas=np.zeros_like(frame)


