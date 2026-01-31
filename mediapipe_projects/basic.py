import cv2
import math
import  mediapipe as mp
from fontTools.misc.cython import returns

cap = cv2.VideoCapture(1)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
while True :
    _, frame = cap.read()
    if not _:
        print("Frame not received")
        continue
    frame = cv2.flip(frame,1)

    #flip_frme = cv2.flip(frame,1)

    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks :
        for hand_lms in result.multi_hand_landmarks :

            for id, lm in enumerate(hand_lms.landmark) :

                h,w,c = frame.shape

                cx,cy = int(lm.x*w), int (lm.y*h)

                if id == 4 :
                    print(f" index finger x = {cx}, y = {cy}")
                    cx4,cy4 = cx,cy
                    cv2.circle(frame,(cx,cy),2,(255,0,0),cv2.FILLED)
                elif id == 8:
                    print(f" thumb finger x = {cx}, y = {cy}")
                    cx8,cy8 =cx,cy
                    cv2.circle(frame,(cx,cy),2,(0,0,255),cv2.FILLED)

            if cx4 and cy4 :
                dist = math.hypot(cx8-cx4,cy8-cy4)
                if dist < 30 :
                    cv2.putText(frame,"click",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()