import cv2
import  mediapipe as mp

cap = cv2.VideoCapture(1)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
while True :
    _, frame = cap.read()
    if not _:
        print("Frame not received")
        continue
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
                    cv2.circle(frame,(cx,cy),10,(255,0,0),cv2.FILLED)
                elif id == 8:
                    cv2.circle(frame,(cx,cy),10,(0,0,255),cv2.FILLED)
                    print(f" thumb finger x = {cx}, y = {cy}")





    frame = cv2.flip(frame,1)
    cv2.imshow("frame", frame)
    
    
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()