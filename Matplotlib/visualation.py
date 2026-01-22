import pandas as pd
import matplotlib.pyplot as plt

final_eye_data={
    "frame" : [1,2,3,4,5,6,7,8,9,10],
    "x_pos" : [111,123,132,143,122,133,142,149,139,129],
    "y_pos" : [211,222,231,218,218,239,234,229,213,210]
}
df=pd.DataFrame(final_eye_data)
df.plot(x="x_pos",y="y_pos",kind="scatter",title="Nabeel's Eyes Movement Map")
plt.xlabel("x_pos")
plt.ylabel("y_pos")
plt.grid(True)
plt.show()
df.to_csv("nabeel",index=False)