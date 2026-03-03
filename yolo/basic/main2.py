import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)


while True :
    count = {"person" : 0,
             "cell phone" : 0 }  
    y_value = 25  
    success,frame = cap.read()
    if success == True :
        frame = cv2.flip(frame,1)
        
        result = model(frame,conf = 0.25,iou = 0.01,verbose = False)
        
        for r in result:
            for box in r.boxes :
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                x1,y1,x2,y2 = map(int,box.xyxy[0])
                
                if cls_id == 0 :
                    color =(0,0,255)
                    object = 'person'
                    label = f"Target : person {conf:.2f}"
                    #count["person"] +=1
                elif cls_id == 67 :
                    object = 'cell phone'
                    color =(0,255,0)
                    label = f"Target : phone {conf:.2f}"
                else :
                    continue
                
                
                
                count[object] += 1
                cv2.putText(frame,label, ((x1-10),(y1-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color, 2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),color,3)
                
                
        for key , val in count.items() :
            if val > 0 :
                text = f"Total {key} : {val}"
                cv2.putText(frame,text,(25,y_value), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color, 2)
                y_value +=25    
                
                
                
                
            
        
        cv2.imshow("frame",frame)
    else :
        print("camera not found")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


    