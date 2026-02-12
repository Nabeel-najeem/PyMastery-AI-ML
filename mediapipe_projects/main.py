import cv2
import numpy as np
import pyautogui as pag

import face_engine as fe
import signal_processor as sp
import calibration as cl

cap = cv2.VideoCapture(0)

ww = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
wh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
screen_w, screen_h = pag.size()
print(screen_w, screen_h)

calib_points = [(100,100),(screen_w-100,100),(100,screen_h-100),(screen_w-100,screen_h-100)]

f=0
n=0



detector = fe.face_detector()
smooth_r = sp.smoother()
smooth_l = sp.smoother()
calib = cl.Deapth_caliibration()


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

    if  n<=3 or   f<=3 :
        cv2.putText(frame, f"calibration required", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if calib.calib_mode == 'Near' :
            cv2.putText(frame, f"sit near to {calib.calib_mode} to camera and press 'n' to calibrate", (300, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if n <= 3 :
                cv2.putText(frame, f"{calib_points[n]}", (300, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pag.moveTo(calib_points[n])
        else :
            cv2.putText(frame, f"sit near to far to camera and press 'n' to calibrate", (300, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if f <=3:
                cv2.putText(frame, f"{calib_points[f]}", (300, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pag.moveTo(calib_points[f])


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

    ranges = calib.get_calibrated_range(treshold_click)

    if ranges is not None:
        x_range , y_range = ranges

        screen_x = np.interp(sxl,x_range,[0,screen_w])
        screen_y = np.interp(syl,y_range,[0,screen_h])
        cv2.putText(frame,f"{screen_x} {screen_y}", (700, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        pag.moveTo(screen_x,screen_y)



    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('n'):
        if n<=3 :
            calib.calib_mode = 'Near'
            calib.capture(sxl,syl,treshold_click)
            print("capturing near")
            n=n+1
    if key == ord('f'):
        if f<=3 :
            calib.calib_mode = 'Far'
            calib.capture(sxl,syl,treshold_click)
            print("capturing far")
            f=f+1



cap.release()
cv2.destroyAllWindows()

