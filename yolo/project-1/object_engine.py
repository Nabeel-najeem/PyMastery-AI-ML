import cv2
from ultralytics import YOLO

class YoloEngine:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
        self.device = '0' # RTX 2050 CUDA 

    def detect_objects(self, frame):
        results = self.model.predict(frame, device=self.device, verbose=False)
        
        detections = []
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = self.model.names[cls]

                # We only care about laptops for this milestone
                if label == 'laptop':
                    # Extract Width and Height from xywh (index 2 and 3)
                    w = float(box.xywh[0][2])
                    h = float(box.xywh[0][3])
                    
                    aspect_ratio = w / h
                    area = w * h

                    # THE LOGIC GATE: Only append if it's Landscape
                    if aspect_ratio > 1.2:
                        detections.append({
                            "box": box.xyxy[0].tolist(),
                            "label": label,
                            "ratio": round(aspect_ratio, 2),
                            "area": int(area)
                        })
        return detections