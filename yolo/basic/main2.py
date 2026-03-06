import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt").to('cuda') 

cap = cv2.VideoCapture(0)

while True:
    
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape 
    overlay = frame.copy()
    
    gate_line_x = w//3
    
    cv2.line(frame,(gate_line_x,0),(gate_line_x,h),(255,255,0),2)
    cv2.rectangle(overlay,(0,0),(gate_line_x,h),(0,0,255),-1)
    frame = cv2.addWeighted(overlay,0.3,frame,0.7,0)
    
    
    count = {"person": 0, "cell phone": 0} 
    result = model(frame, conf=0.25, iou=0.01, verbose=False)
    
    for r in result:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            if cls_id == 0:
                obj_name, color = "person", (0, 0, 255) # Red
                cx = (x1+x2)//2
                if cx < gate_line_x :
                    cv2.putText(frame, f"entered restricted area !!", (500, 400), 
                                cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255), 2)
                        
                
            elif cls_id == 67:
                obj_name, color = "cell phone", (0, 255, 0) 
            else:
                continue
            
            count[obj_name] += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{obj_name} {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    alert_mode = count["person"] > 2
    
    if alert_mode:
        cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 30)
        cv2.putText(frame, "!!! ALERT: CROWD !!!", (w//4, h-50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)

    y_val = 40
    for key, val in count.items():
        if val > 0:
            txt_color = (0, 255, 255) if alert_mode else (255, 255, 255)
            cv2.putText(frame, f"Total {key}: {val}", (20, y_val), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, txt_color, 2)
            y_val += 35


    
    cv2.imshow("Hexer AI Security System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()