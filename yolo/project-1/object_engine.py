import cv2
from ultralytics import YOLO

class YoloEngine:
    def __init__(self, model_path='yolov8n.pt'):
        # Initialize the model on the GPU (RTX 2050)
        self.model = YOLO(model_path)
        self.device = 'cuda'

    def detect_objects(self, frame):
        # Run inference
        results = self.model.predict(frame, device=self.device, verbose=False)
        
        detections = []
        for r in results:
            for box in r.boxes:
                # Extract coordinates, class, and confidence
                coords = box.xyxy[0].tolist() 
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                
                detections.append({
                    "box": coords,
                    "class": self.model.names[cls],
                    "conf": conf
                })
        return detections