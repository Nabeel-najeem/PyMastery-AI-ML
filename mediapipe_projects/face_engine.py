import cv2
import math
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
        self.curent_landmarks = None

    def find_face_data(self,frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks :
            self.curent_landmarks = results.multi_face_landmarks[0].landmark
            return self.curent_landmarks
        self.curent_landmarks = None
        return []


    def x_y_landmarks(self,frame,id):
        if self.curent_landmarks is None :
            return None,None
        h,w,_ = frame.shape
        lm = self.curent_landmarks[id]
        x = int(lm.x*w)
        y = int(lm.y*h)
        return x,y


    def dynamic_treshold(self,frame):
        fhx,fhy = self.x_y_landmarks(frame,10)
        lhx,lhy = self.x_y_landmarks(frame,103)
        rhx,rhy = self.x_y_landmarks(frame,332)

        if None in [lhx,lhy,rhx,rhy,fhx,fhy]:
            return None
        dis_fh_lh = math.hypot(fhx-lhx,fhy-lhy)
        dis_lh_rh = math.hypot(lhx-rhx,lhy-rhy)
        dis_fh_rh = math.hypot(fhx-rhx,fhy-lhy)

        treshold = ((dis_fh_rh+ dis_fh_lh+ dis_lh_rh)/3)/9.7
        return treshold

    def click (self,frame, id_1, id_2):
        id_1x, id_1y = self.x_y_landmarks(frame,id_1)
        id_2x, id_2y = self.x_y_landmarks(frame,id_2)
        if id_1x is not None and id_2x is not None:
            dis_btw_id1_id2 = math.hypot(id_1x - id_2x, id_1y - id_2y)
            return dis_btw_id1_id2
        return None














