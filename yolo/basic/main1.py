from ultralytics import YOLO

model = YOLO('yolov8n.pt')

image = r"C:\Users\najee\Desktop\Python_expert\yolo\project-2\bus.jpg"

results = model(image,conf = 0.25,iou = 0.5)
class_names = model.names

###
res = results[0]
orgin_shape = res.orig_shape
print(f"original shape : {orgin_shape}")

speed_dict = res.speed
fps = 1000/speed_dict['inference']
print(f"interface speed : {speed_dict['inference']:.2f}ms | fps :{fps:.2f}")
###

for r in results:
    print(f"detected {len(r.boxes)} object after nms")
    for box in r.boxes :
        cls_id = int(box.cls[0])
        if cls_id == 3 :
            print(f"Alert : motorcycle detcted with {box.conf[0]}")
        name = class_names[cls_id]
        print(f"id : {cls_id} is a {name}")

    
        