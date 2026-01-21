import pandas as pd
tracker_log={
    "frame_id" : [1,2,3,4],
    "pupil_x" : [120,122,121,119],
    "pupil_y" : [200, 205, 202, 201],
    "status" : ["Detected", "Detected", "Blink", "Detected"]
}
eye_df=pd.DataFrame(tracker_log)
print(eye_df)
print(eye_df.describe())