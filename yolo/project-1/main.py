import cv2

import object_engine





cap = cv2.VideoCapture(0)



while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame,1)















    cv2.imshow('frame',frame)



    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()