import cv2
import mediapipe as mp
import numpy as np
import math
import pyautogui as pag

def empth(x):
    pass
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands
hand = hands.Hands()
drawing_util = mp.solutions.drawing_utils
ww = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
wh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cx4,cy4,cx8,cy8 = 0,0,0,0

px, py = 0,0
#smooh_factor  = 6

alpha = 6

min_alpha = 0.05
max_alpha = 0.9
dead_zone = 5

screen_w, screen_h = pag.size()
is_draging = False


"""
cv2.namedWindow("ratio for window")
cv2.resizeWindow("ratio for window",300,75)
cv2.createTrackbar("ratio value","ratio for window",1,100,empth)

"""

while True :

    pag.PAUSE = 0

    m_ratio = 4.5#cv2.getTrackbarPos("ratio value","ratio for window")
    ratio_x = 1 * m_ratio
    ration_y = 0.5625 * m_ratio


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
                    cv2.circle(frame,(cx4,cy4),3,(0,0,255),cv2.FILLED)
                elif id == 8 :
                    cx8,cy8 = cx, cy

                elif id == 12 :
                    cx12, cy12 = cx, cy
                    cv2.circle(frame,(cx12,cy12),3,(255,255,0),cv2.FILLED)


                elif id == 0 :
                    cx0, cy0 = cx, cy

                elif id == 9 :
                    cx9, cy9 = cx, cy



            if cx4 !=0 and cx8!=0 :
                x_mouse = np.interp(cx8,[0,ww],[0,sw])
                y_mouse = np.interp(cy8,[0,wh],[0,sh])

                cv2.putText(frame,f"{x_mouse} {y_mouse}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                #scx ,scy = px+(x_mouse-px)/smooh_factor,py+(y_mouse-py)/smooh_factor

                velocity = math.hypot(x_mouse-px, y_mouse-py)
                alpha = np.interp(velocity, [0, 50], [min_alpha, max_alpha])
                cv2.putText(frame,f"{alpha}",(800,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

                ref_dist = math.hypot(cx9-cx0, cy9-cy0)

                center_x, center_y = sw//2, sh//2
                cv2.circle(frame, (center_x, center_y), 3, (1, 1, 1), cv2.FILLED)
                cv2.putText(frame,f"{sw}   {sh}",(500,600),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

                bound_w = int(ref_dist*ratio_x)
                bound_h = int(ref_dist*ration_y)

                box_x1, box_x2 = center_x - bound_w//2, center_x + bound_w//2
                box_y1, box_y2 = center_y - bound_h//2, center_y + bound_h//2



                scx = (alpha*x_mouse) + ((1-alpha)*px)
                scy = (alpha*y_mouse) + ((1-alpha)*py)

                actual_x = np.interp(scx,(box_x1,box_x2),(0,screen_w))
                actual_y = np.interp(scy,(box_y1,box_y2),(0,screen_h))

                movement_dist = math.hypot(x_mouse-px, y_mouse-py)
                if movement_dist < dead_zone :
                    scx, scy = px, py
                    status = "stable"
                else :
                    px, py = scx,scy
                    status = "unstable"
                cv2.putText(frame,f"{status}", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
                if 100 < scx < 1100 and 100 < scy < 600 :

                    cv2.circle(frame,(int(x_mouse),int(y_mouse)),3,(0,0,255),cv2.FILLED)
                    cv2.circle(frame,(int(scx),int(scy)),3,(0,255,0),cv2.FILLED)
                    cv2.putText(frame,f"{scx} {scy}",(100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

            dynamic_treshold = ref_dist * 0.18
            mouse_dynamic_treshold = ref_dist * 0.27


            cv2.putText(frame,f"n-{dynamic_treshold}",(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            cv2.putText(frame, f"m-{mouse_dynamic_treshold}", (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if cx4 and cx8 :
                distance = math.hypot(cx8-cx4, cy8-cy4)
                if distance < dynamic_treshold :
                    if not is_draging :
                        pag.mouseDown()
                        is_draging = True
                    cv2.putText(frame,"click",(1100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                else :
                    if is_draging :
                        pag.mouseUp()
                        is_draging = False
                    #pag.click()

            if cx4 and cx12 :
                distance = math.hypot(cx12-cx4, cy12-cy4)
                if distance < dynamic_treshold :
                    pag.rightClick()

            if cx8 and cx12 :
                distance = math.hypot(cx12-cx8, cy12-cy8)
                if distance < mouse_dynamic_treshold:
                    cv2.putText(frame,"scrool",(1100,500),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                    scroll_amount = (y_mouse-py)*2
                    if abs(scroll_amount) > 2 :
                        pag.scroll(-int(scroll_amount))

            pag.moveTo(actual_x,actual_y)
            if is_draging == False :
                color = 0,0,255
            elif is_draging == True :
                color = 0,255,255


            cv2.rectangle(frame,(box_x1,box_y1),(box_x2,box_y2),(color),2)


    cv2.imshow("frame",frame)
    if cv2.waitKey(1)&0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()




