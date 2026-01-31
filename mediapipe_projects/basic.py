import cv2
import mediapipe as mp
 
h =mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
while True :
    success,frame = cap.read()
    frame=cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = h.process(rgb_frame)
    
    
    
    
    
    
    
    
    
    cv2.imshow("feed",result)
    
    key = cv2.waitKey(1) &0xFF
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()