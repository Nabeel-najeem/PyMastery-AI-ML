import math

import cv2
import face_engine as fe

cap = cv2.VideoCapture(0)

detector = fe.face_detector()

while True:
    success,frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame,1)

    landmarks = detector.find_face_data(frame)


    #pupils
    xr,yr = detector.x_y_landmarks(frame=frame,id=468)
    xl,yl = detector.x_y_landmarks(frame=frame,id=473)
    if xr and yr is not None:
        cv2.circle(frame, (xr, yr), 3, (0, 0, 255), cv2.FILLED)
        cv2.circle(frame, (xl, yl), 3, (0, 0, 255), cv2.FILLED)

    #dynamic treshold
    treshold_click = detector.dynamic_treshold(frame)
    cv2.putText(frame, f"treshold-{treshold_click}", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 2)

    #rightt eye lice
    retx ,rety = detector.x_y_landmarks(frame=frame,id=386)
    relx, rely = detector.x_y_landmarks(frame=frame,id=374)
    if retx and relx is not None:
        right_eye_distance = math.hypot(retx-relx,rety-rely)
        cv2.putText(frame, f"distance-{right_eye_distance}", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.circle(frame, (retx, rety), 1, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (relx, rely), 1, (255, 0, 255), cv2.FILLED)

    #left eye lice
    letx ,lety = detector.x_y_landmarks(frame=frame,id=159)
    lelx, lely = detector.x_y_landmarks(frame=frame,id=145)
    if retx and relx is not None:
        left_eye_distance = math.hypot(letx-lelx,lety-lely)
        cv2.putText(frame, f"distance-{left_eye_distance}", (100, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.circle(frame, (letx, lety), 1, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (lelx, lely), 1, (255, 0, 255), cv2.FILLED)

    #click logic
    if right_eye_distance and left_eye_distance :
        avg_distance = (right_eye_distance + left_eye_distance)/2
        if avg_distance < treshold_click :
            cv2.putText(frame, f"click", (1000, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


