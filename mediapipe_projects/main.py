import cv2
import face_engine as fe

cap = cv2.VideoCapture(0)



detector = fe.face_detector()
right_eye = fe.face_detector()

while True:
    success,frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame,1)

    landmarks = detector.find_face_data(frame)
    x,y,z = right_eye.find_pupils(frame)
    if x :
        cv2.circle(frame, (x, y), 3, (0, 0, 255), cv2.FILLED)
        #cv2.putText(frame,f"{eye}",(100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
    length = len(landmarks)
    if not length == 0 :
        cv2.putText(frame,f"{length}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))



    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
