from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results=model(r"C:\Users\najee\Desktop\Python_expert\yolo\project-2\image.png",device = 0,save = True,project= "yolo",name = "project-2")
'''print(f"detected object : {r.names}")
print(f"boxes : {r.boxes}")'''
for r in results :
    names = r.names
    
    for box in r.boxes :
        cls_id = int(box.cls[0])
        label = names[cls_id]
        
        w = float(box.xywh[0][2])
        h = float(box.xywh[0][3])
        
        area = w*h
        aspect_ratio = w / h
        
        print(f"object : {label} | Area : {area:.2f}px | Ratio : {aspect_ratio:.2f}")
        
        