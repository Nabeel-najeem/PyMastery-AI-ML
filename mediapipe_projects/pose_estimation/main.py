import cv2
import pyautogui as pag
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

command_active = False
shurg_cooldown = 0

posture_timer = 0
Alert_treshold = 90
cap = cv2.VideoCapture(0)


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

    if is_shurg and angle > 150 :
        if shurg_cooldown ==0 :
            command_active  = not command_active
            shurg_cooldown = 20
            pag.press('volumemute')


    if shurg_cooldown > 0 :
        shurg_cooldown -= 1

    if command_active :
        color = (0, 255, 0)
        status = "system : Active"
    else :
        color = (0, 0, 255)
        status = "system : idle"
    cv2.putText(frame, f"{status}", (100, 260), cv2.FONT_HERSHEY_SIMPLEX, 1,color, 2)



    curent_posture = pose.get_posture(pose_lms)
    if curent_posture != "GOOD POSTURE":
        posture_timer += 1
    else :
        posture_timer = 0

    if posture_timer > Alert_treshold:
        cv2.putText(frame, f"fix you posture", (700, 100), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)



    cv2.imshow('frame',frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
