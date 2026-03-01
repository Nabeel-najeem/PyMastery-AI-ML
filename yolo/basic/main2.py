import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True :
    success,frame = cap.read()
    if success == True :
        frame = cv2.flip(frame,1)
        
        result = model(frame,conf = 0.25,iou = 0.01,verbose = False)
        
        for r in result:
            for box in r.boxes :
                cls_id = int(box.cls[0])
                if cls_id == 0 :
                    x1,y1,x2,y2 = box.xyxy[0].tolist()
                    cv2.putText(frame,f"person detected", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    print("person detected")
                    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                    cv2.putText(frame,f"person detected", ((x1-10),(y1-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)
            
        
        cv2.imshow("frame",frame)
    else :
        print("camera not found")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    