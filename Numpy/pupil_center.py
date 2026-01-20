import numpy as np
detected_pupil=np.random.randint(1,256,(5,2))
print(detected_pupil)
final_mouse_pose=np.mean(detected_pupil,axis=0)
print(final_mouse_pose)
print(detected_pupil.reshape(10))