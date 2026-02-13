import cv2
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
            return self.curent_result.pose_landmarks
        return None
    def get_body_tilt(self,landmarks):
        if landmarks :
            left_sholder = landmarks[11]
            right_sholder = landmarks[12]
            tile = (left_sholder.x + right_sholder.x)/2
            return tile
        return 0.5

