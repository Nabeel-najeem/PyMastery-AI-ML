import cv2
import mediapipe as mp

class face_detector:
    def __init__(self,refine = True):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            min_detection_confidence=0.5,
            refine_landmarks=refine
        )

    def find_face_data(self,frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        face_data = []
        if results.multi_face_landmarks :
            for face_lms in results.multi_face_landmarks :
                face_data.append(face_lms.landmark)
        return face_data

    def x_y_landmarks(self,frame,id):
        h,w,_ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        if results.multi_face_landmarks :
            face_lms = results.multi_face_landmarks[0]

            lm = face_lms.landmark[id]

            x = int(lm.x*w)
            y = int(lm.y*h)

            return x,y
        return None,None






