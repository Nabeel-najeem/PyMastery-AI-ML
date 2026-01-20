import numpy as np

eye_grid=np.random.randint(1,256,(3,3))
print(eye_grid)

print("")
min_eye_grid=np.min(eye_grid)
print(min_eye_grid)
print("")
min_index_eye_grid=np.argmin(eye_grid)
print(min_index_eye_grid)
print("")
row,col=np.unravel_index(min_index_eye_grid,eye_grid.shape)
print(f"row : {row} coloum : {col}")