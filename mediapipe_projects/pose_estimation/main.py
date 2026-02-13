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
    if pose_lms is not None:
        mp_drawing.draw_landmarks(frame,pose_lms,mp_pose.POSE_CONNECTIONS)


    cv2.imshow('frame',frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
