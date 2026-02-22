import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")

known_width = 9.0
focal_length = 650

cap = cv2.VideoCapture(0)

while True :
    sucess,frame = cap.read()
    if not sucess : 
        break
    frame = cv2.flip(frame,1)
    
    result = model.track(frame,persist=True,device = 0, verbose = False)
    
    for r in result :
        boxes = r.boxes
        for box in boxes :
            cls_id = int(box.cls[0])
            label = r.names[cls_id]
            
            if label == "cell phone" :
                
                w_pixel = float(box.xywh[0][2])
                
                distance = (known_width*focal_length)/w_pixel
                
                x1,y1,x2,y2 = map(int,box.xyxy[0])
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame,f"distance : {distance: .1f}cm",(x1,y1-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.6,(0,255,0),2)
    
    
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    