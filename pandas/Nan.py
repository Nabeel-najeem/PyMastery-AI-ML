import pandas as pd
import numpy as np
meesy_log={
    "Frame" : [1,2,3,4,5],
    "pupil_x" : [110,np.nan,115,np.nan,112],
    "status" : ["detected","error","detected","error","detected"]
}

df=pd.DataFrame(meesy_log)
clean_df=df.fillna(0)
analyse=df.groupby('status')["Frame"].count()
clean_df.to_csv("nabeel_cleaned_logs.csv", index=False)