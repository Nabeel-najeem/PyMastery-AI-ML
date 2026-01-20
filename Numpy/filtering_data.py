import numpy as np
sensor_data=np.array([120, 130, 999, 125, 1000, 115])
mask= sensor_data < 500
clean_data=sensor_data[mask]
print(np.mean(clean_data))