import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

image_path = r"C:\Users\najee\Desktop\Python_expert\yolo\project-2\image.png"

results = model(
    image_path,
    device=0,       
    save=False,
    project="yolo",
    name="project-2"
)

for r in results:
    names = r.names
    boxes = r.boxes

    img = cv2.imread(image_path)

    counts = {}

    if boxes is not None:
        for box in boxes:
            cls_id = int(box.cls[0])
            label = names[cls_id]

            counts[label] = counts.get(label, 0) + 1

            w = float(box.xywh[0][2])
            h = float(box.xywh[0][3])

            area = w * h
            aspect_ratio = w / h if h != 0 else 0

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            text = f"{label} | A:{area:.2f} | R:{aspect_ratio:.2f}"
            cv2.putText(img, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            print(f"Object: {label} | Area: {area:.2f}px | Ratio: {aspect_ratio:.2f}")

    print("\n===== Object Summary =====")
    for obj, count in counts.items():
        print(f"{obj}: {count}")

    cv2.imshow("YOLO Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()