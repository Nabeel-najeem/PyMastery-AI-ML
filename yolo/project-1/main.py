import cv2
from object_engine import YoloEngine

engine = YoloEngine()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)

    # 1. Run Detection
    results = engine.detect_objects(frame)

    # 2. Process Results
    for data in results:
        # Draw the box for visual feedback
        x1, y1, x2, y2 = map(int, data['box'])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Telemetry Text
        info = f"Ratio: {data['ratio']} | Area: {data['area']}"
        cv2.putText(frame, info, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Terminal Output for the Task
        print(f"✅ Landscape Laptop Found: {info}")

    cv2.imshow('Hexer YOLO - Module 1', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()