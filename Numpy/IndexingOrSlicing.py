import numpy as np

camera_frame=np.random.randint(1,256,(4,4))
print("Camera Frame")
print(camera_frame)
print("indexing")
print(camera_frame[2,3])
print("eye region")
eye_region=camera_frame[1:3,1:3]
print(eye_region)
print("brightest eye region")
brightest_eye_region=eye_region*1.5
print(brightest_eye_region)