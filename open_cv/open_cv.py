import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.line(frame, (0, 0), (200, 200), (255, 0, 0), 5)
    cv2.rectangle(frame, (350, 10), (500, 150), (0, 255, 0), 3)
    cv2.circle(frame, (256, 256), 50, (0, 0, 255), -1)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Live Feed', (10, 450), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Live Drawing', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()