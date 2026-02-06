import cv2
import mediapipe as mp

from mediapipe_projects.basic import mp_drawing

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True :
    success,frame = cap.read()
    if not success:
        print ("cam not found ")
        break


    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb_frame)
    if result.multi_face_landmarks :
        for face_lms in result.multi_face_landmarks :
            mp_drawing.draw_landmarks(
                image=rgb_frame,
                landmark_list=face_lms,
                connections=face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None ,
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=2,))



    cv2.imshow('frame',rgb_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
