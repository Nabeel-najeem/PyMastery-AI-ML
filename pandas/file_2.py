import pandas as pd
tracker_log={
    "frame_id" : [1,2,3,4],
    "pupil_x" : [120,122,121,119],
    "pupil_y" : [200, 205, 202, 201],
    "status" : ["Detected", "Detected", "Blink", "Detected"]
}
eye_df=pd.DataFrame(tracker_log)
y_cord=eye_df["pupil_y"]
print(y_cord)
detected_only = eye_df[eye_df["status"] == "Detected"]
print(detected_only)
eye_df["shift_x"]=eye_df["pupil_x"]-120
print(eye_df)