import numpy as np

frame = np.random.randint(100,256,(6,6))
frame[3,3]=10
#print(frame)
eye_region=frame[2:5,2:5]
#print(eye_region)
mask= eye_region > 200
#print(mask)
eye_region[mask]=0
print(eye_region)
min_point_eye_region=np.argmin(eye_region)
row,col=np.unravel_index(min_point_eye_region,np.shape(eye_region))
print(f"\n coordinate of pupil is row : {row} coloum : {col}")