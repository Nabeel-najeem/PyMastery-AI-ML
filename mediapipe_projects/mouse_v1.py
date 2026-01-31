import cv2
import mediapipe as mp
import numpy as np
import math

cap = cv2.VideoCapture(1)
hands = mp.solutions.hands
hand = hands.Hands()
drawing_util = mp.solutions.drawing_utils
ww = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
wh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cx4,cy4,cx8,cy8 = 0,0,0,0




while True :
    _,frame=cap.read()
    if not _ :
        print("cam not found")
        continue

    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(rgb_frame)
    if result.multi_hand_landmarks :
        for hand_lms in result.multi_hand_landmarks :
            for id , lm in enumerate(hand_lms.landmark) :
                sh,sw,c = frame.shape
                #print(f"{h} x {w} x {c}")
                cx,cy = int(lm.x*sw),int(lm.y*sh)

                if id == 4 :
                    cx4,cy4 = cx, cy
                    #cv2.circle(frame,(cx4,cy4),3,(0,0,255),cv2.FILLED)
                elif id == 8 :
                    cx8,cy8 = cx, cy
                    #cv2.circle(frame,(cx8,cy8),3,(0,255,0),cv2.FILLED)

                if cx4 !=0 and cx8!=0 :
                    x_mouse = np.interp(cx8,[0,ww],[0,sw])
                    y_mouse = np.interp(cy8,[0,wh],[0,sh])
                    cv2.putText(frame,f"{x_mouse} {y_mouse}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                    if 100 < x_mouse < 1100 and 100 < y_mouse < 600 :
                        cv2.circle(frame,(int(x_mouse),int(y_mouse)),3,(0,255,255),cv2.FILLED)
                if cx4 and cx8 :
                    distance = math.hypot(cx8-cx4, cy8-cy8)
                    if distance < 20 :
                        cv2.putText(frame,"click",(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.rectangle(frame,(100,100),(1100,600),(0,0,255),2)


    cv2.imshow("frame",frame)
    if cv2.waitKey(1)&0xFF == ord('q') :
        break