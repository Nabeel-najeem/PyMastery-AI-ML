import cv2
import pyautogui as pag

import face_engine as fe
import signal_processor as sp

cap = cv2.VideoCapture(0)

ww = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
wh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
screen_w, screen_h = pag.size()


detector = fe.face_detector()
smooth_r = sp.smoother()
smooth_l = sp.smoother()

while True:
    success,frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame,1)
    landmarks = detector.find_face_data(frame)


    #pupils
    xl,yl = detector.x_y_landmarks(frame=frame,id=468)
    xr,yr = detector.x_y_landmarks(frame=frame,id=473)
    if xr is not None and yr is not None:
        cv2.circle(frame, (xr, yr), 3, (0, 0, 255), cv2.FILLED)
        cv2.circle(frame, (xl, yl), 3, (0, 0, 255), cv2.FILLED)

    sxr,syr,dar,sr = smooth_r.smooth(xr,yr)
    sxl,syl,dal,sl = smooth_l.smooth(xl,yl)
    if not None in [sxr,syr,dar,sxl,syl,dal]:
        cv2.circle(frame, (sxr, syr), 3, (0, 255, 255), cv2.FILLED)
        cv2.circle(frame, (sxl, syl), 3, (0, 255, 255), cv2.FILLED)
        if sr == True and sl == True :
            cv2.putText(frame, f"stable", (900, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if sr == False and sl == False :
            cv2.putText(frame, f"unstable", (900, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    #dynamic treshold
    treshold_click = detector.dynamic_treshold(frame)
    cv2.putText(frame, f"treshold-{treshold_click}", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 2)


    #click logic
    left_eye = detector.click(frame,159,145)
    right_eye = detector.click(frame,386,374)
    if left_eye is not None and right_eye is not None:
        cv2.putText(frame,f"right - {right_eye} and left - {left_eye}", (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        avg_dis = (left_eye+right_eye)/2
        if  avg_dis  < treshold_click :
            cv2.putText(frame,"click", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

