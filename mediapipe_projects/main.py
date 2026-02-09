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

    xr,yr = detector.x_y_landmarks(frame=frame,id=468)
    xl,yl = detector.x_y_landmarks(frame=frame,id=473)
    if xr and yr is not None:
        cv2.circle(frame, (xr, yr), 3, (0, 0, 255), cv2.FILLED)
        cv2.circle(frame, (xl, yl), 3, (0, 0, 255), cv2.FILLED)


    length = len(landmarks)
    if  length != 0 :
        cv2.putText(frame,f"{length}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))



    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


