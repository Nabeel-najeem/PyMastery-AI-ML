import cv2
from ultralytics import YOLO

# 1. Load the model - Moving to GPU for better FPS on your RTX 2050
model = YOLO("yolov8n.pt").to('cuda') 

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape  # Get dimensions for the border
    
    # Reset counts for every frame
    count = {"person": 0, "cell phone": 0} 
    result = model(frame, conf=0.25, iou=0.01, verbose=False)
    
    # --- DETECTION LOOP ---
    for r in result:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            if cls_id == 0:
                obj_name, color = "person", (0, 0, 255) # Red
            elif cls_id == 67:
                obj_name, color = "cell phone", (0, 255, 0) # Green
            else:
                continue
            
            count[obj_name] += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{obj_name} {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # --- THE ALERT LOGIC ---
    # Trigger alarm if more than 2 people are detected
    alert_mode = count["person"] > 2
    
    if alert_mode:
        # Draw a thick RED border around the whole screen
        cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 30)
        cv2.putText(frame, "!!! ALERT: CROWD !!!", (w//4, h-50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)

    # --- UI DASHBOARD ---
    y_val = 40
    for key, val in count.items():
        if val > 0:
            # If alert is on, text turns YELLOW to stand out
            txt_color = (0, 255, 255) if alert_mode else (255, 255, 255)
            cv2.putText(frame, f"Total {key}: {val}", (20, y_val), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, txt_color, 2)
            y_val += 35

    cv2.imshow("Hexer AI Security System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()