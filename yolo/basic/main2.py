import sqlite3
import os
import cv2
import time
import datetime
from ultralytics import YOLO

def init_db():
    conn = sqlite3.connect("hexer_security.db")
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS intruders(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,person_id INTEGER,
                       timestamp TEXT)""")
    conn.commit()
    return conn,cursor

conn,cursor = init_db()
def sync_memory():

    cursor.execute("SELECT id FROM intruders")
    rows = cursor.fetchall()
    for row in rows :
        person_ids.add(row[0])
    print(f"Synced {len(person_ids)} history records")
    
    
    
model = YOLO("yolov8n.pt").to("cuda")

cap = cv2.VideoCapture(0)

person_ids = set()
p_time = 0

if not os.path.exists("intruders"):
    os.makedirs("intruders")

last_log_time = {}

sync_memory()
start_time = time .time()
while True:
    intruder_detected_this_frame = False
    current_intruder_id = None

    success, frame = cap.read()
    if not success:
        break
    
    c_time = time.time()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ScreenTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    today_folder = datetime.datetime.now().strftime("%Y-%m-%d")
    save_path = f"intruders/{today_folder}"
    
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    
    
    if p_time != 0 :
        fps = 1/(c_time - p_time)
    else :
        fps = 0
    p_time = c_time

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    overlay = frame.copy()
    gate_line_x = w // 3
    warning_line = w//2
    critical_line = w//4

    cv2.line(frame, (gate_line_x, 0), (gate_line_x, h), (255,255,0), 2)

    cv2.rectangle(overlay, (0,0), (gate_line_x,h), (0,0,255), -1)

    count = {"person":0, "cell phone":0}

    results = model.track(
        frame,
        persist=True,
        conf=0.25,
        iou=0.3,
        verbose=False
    )

    for r in results:

        if r.boxes.id is None:
            continue

        ids = r.boxes.id.int().cpu().tolist()

        for box, obj_id in zip(r.boxes, ids):

            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if cls_id == 0:

                obj_name = "person"
                color = (0,0,255)


                cx = (x1 + x2) // 2

                
                if cx < warning_line and cx > critical_line :
                    cv2.putText(frame, "WARNING: RESTRICTED AREA AHEAD", (w//2, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
                    cv2.line(frame, (warning_line, 0), (warning_line, h), (0, 255, 255), 2)
                elif cx <= critical_line :
                    cv2.putText(frame, "!!! CRITICAL BREACH !!!", (w//2, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                elif cx < gate_line_x:
                    cv2.putText(frame,f"Entered Restricted Area!",(400, 100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cursor.execute("SELECT id FROM intruders WHERE id = ?",(obj_id,))
                    data = cursor.fetchone()
                    intruder_detected_this_frame = True
                    current_intruder_id = obj_id
                    if obj_id not in person_ids  : 
                        person_ids.add(obj_id)
                        
                            

            elif cls_id == 67:

                obj_name = "cell phone"
                color = (0,255,0)

            else:
                continue

            count[obj_name] += 1

            cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)

            cv2.putText(
                frame,
                f"{obj_name} | {conf:.2f} | ID:{obj_id}",
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2
            )

    alert_mode = count["person"] > 2

    if alert_mode:
        cv2.rectangle(frame, (0,0), (w,h), (0,0,255), 30)
        cv2.putText(
            frame,
            "!!! ALERT: CROWD !!!",
            (w//4, h-50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0,0,255),
            4
        )
    

    y_val = 40
    for key, val in count.items():

        if val > 0:

            txt_color = (0,255,255) if alert_mode else (255,255,255)

            cv2.putText(
                frame,
                f"{key}: {val}",
                (20, y_val),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                txt_color,
                2
            )

            y_val += 35
            
    frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)
   
    cv2.putText(frame,f"total {len(person_ids)} person enterd in restricted area ",(600, 120),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.putText(frame,f"FPS : {int(fps)}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,255),4)
    cv2.putText(frame,f"{ScreenTimeStamp}",(800,50),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),4)
    
    if intruder_detected_this_frame :
        if current_intruder_id not in last_log_time or (c_time - last_log_time[current_intruder_id]) > 30 :
            cv2.imwrite(f"{save_path}/intruder_{current_intruder_id}_{timestamp}.jpg",frame)
            cursor.execute("INSERT INTO intruders (person_id,timestamp) values (?,?)",(current_intruder_id,timestamp))
            conn.commit()
            print(f"evidence saved for {current_intruder_id}")
            last_log_time[current_intruder_id] = c_time
            log_file_path = f"{save_path}/daily_report.txt"
            with open(log_file_path,"a") as f :
                f.write(f"ID : {current_intruder_id} | Time : {ScreenTimeStamp}\n" )
    uptime = int(time.time() - start_time)

    cv2.rectangle(frame, (0, 680), (370, 715), (0, 0, 0), -1) 
    status_text = f"DB: Connected | AI: YOLOv8n | uptime : {uptime} s"
    cv2.putText(frame, status_text, (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
conn.close()
print("Database connection closed safely")