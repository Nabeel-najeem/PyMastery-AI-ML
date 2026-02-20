from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results=model(r"C:\Users\najee\Desktop\Python_expert\yolo\project-2\image.png",device = 0,save = True,project= "yolo",name = "project-2")
for r in results :
    print(f"detected object : {r.names}")
    print(f"boxes : {r.boxes}")