import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


import pose_engine as pe
pose = pe.possDetector()


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame,1)

    pose_lms = pose.find_pose(frame)

    is_shurg = pose.get_shrug(pose_lms)
    if is_shurg == True:
        cv2.putText(frame, f"shurg detected", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    angle = pose.get_angle(pose_lms,11,13,15)
    if angle != None:
        cv2.putText(frame, f"{angle}", (100, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('frame',frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
