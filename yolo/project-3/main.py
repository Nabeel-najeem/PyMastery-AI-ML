import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

real_width = {"cell phone": 7.5,
              "bottle": 7.0,
              "person" : 36,
              }
focal_length = 650
cap = cv2.VideoCapture(0)


track_history = {}

while True:
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)
    current_time = time.time()
    
    results = model.track(frame, persist=True, device=0, verbose=False)
    
    for r in results:
        if r.boxes.id is not None:
            boxes = r.boxes.xywh.cpu()
            track_ids = r.boxes.id.int().cpu().tolist()
            cls_ids = r.boxes.cls.int().cpu().tolist()

            for box, track_id, cls_id in zip(boxes, track_ids, cls_ids):
                label = r.names[cls_id]
                
                if label in real_width:
                    w_pixel = float(box[2])
                    distance = (real_width[label] * focal_length) / w_pixel
                    
                    speed = 0
                    if track_id in track_history:
                        prev_dist, prev_time = track_history[track_id]
                        
                        delta_d = abs(prev_dist - distance)
                        delta_t = current_time - prev_time
                        
                        if delta_t > 0:
                            speed = delta_d / delta_t 
                    
                    track_history[track_id] = (distance, current_time)

                    x, y, w, h = box
                    x1, y1 = int(x - w/2), int(y - h/2)
                    cv2.putText(frame, f"Dist: {distance:.1f}cm", (x1, y1-10), 0, 0.5, (0,255,0), 2)
                    cv2.putText(frame, f"Speed: {speed:.1f}cm/s", (x1, y1-30), 0, 0.5, (255,0,0), 2)
                    cv2.rectangle(frame, (x1, y1), (int(x+w/2), int(y+h/2)), (0,255,0), 2)

    cv2.imshow("Velocity Engine - Day 41", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()