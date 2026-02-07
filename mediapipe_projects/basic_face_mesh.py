import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

mp_face_mesh = mp.solutions.face_mesh
mp_drawing_utils = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

while True :
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #landmark detection

    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks :
        for face_landmark in result.multi_face_landmarks :
            mp_drawing_utils.draw_landmarks(
                image = frame,
                landmark_list = face_landmark,
                connections = mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec = None,
                connection_drawing_spec = mp_drawing_style.get_default_face_mesh_iris_connections_style()
            )

            mp_drawing_utils.draw_landmarks(
                image = frame,
                landmark_list = face_landmark,
                connections = mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec = None,
                connection_drawing_spec = mp_drawing_style.get_default_face_mesh_contours_style()
            )

            mp_drawing_utils.draw_landmarks(
                image = frame,
                landmark_list = face_landmark,
                connections = mp_face_mesh.FACEMESH_NOSE,
                landmark_drawing_spec = None,
                connection_drawing_spec = mp_drawing_style.get_default_face_mesh_tesselation_style()
            )



    cv2.imshow('rgb frame',frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()