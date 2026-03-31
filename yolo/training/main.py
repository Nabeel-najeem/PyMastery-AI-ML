from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data = "hexer_data.yaml",
    epochs = 50,
    imgsz=640,
    device = 0
)

