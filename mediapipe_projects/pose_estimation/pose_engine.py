import cv2
import math
import mediapipe as mp

class possDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.curent_result = None

    def find_pose(self,frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.curent_result = self.pose.process(rgb_frame)

        if self.curent_result.pose_landmarks:
            return self.curent_result.pose_landmarks.landmark
        return None
    def get_body_tilt(self,landmarks):
        if landmarks :
            left_sholder = landmarks[11]
            right_sholder = landmarks[12]
            tile = (left_sholder.x + right_sholder.x)/2
            return tile
        return 0.5

    def get_shrug(self,landmarks):
        if landmarks :

            left_ear_y = landmarks[7].y
            left_shoulder_y = landmarks[11].y

            right_ear_y = landmarks[8].y
            right_shoulder_y = landmarks[12].y

            left_shurg_dist = left_shoulder_y - left_ear_y
            right_shurg_dist = right_shoulder_y - right_ear_y

            if left_shurg_dist < 0.3 and right_shurg_dist < 0.3 :
                return True
        return False

    def get_angle(self,landmarks,p1,p2,p3):
        if landmarks != None:
            left_sholder = landmarks[11]
            x1, y1 = landmarks[p1].x, landmarks[p1].y
            x2, y2 = landmarks[p2].x, landmarks[p2].y
            x3, y3 = landmarks[p3].x, landmarks[p3].y

            angle = math.degrees(math.atan2(y3-y2,x3-x2)-
                                 math.atan2(y1-y2,x1-x2))

            angle =abs(angle)
            if angle > 180 :
                angle = 360-angle
            return angle
        return None


