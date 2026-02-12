import numpy as np

class Deapth_caliibration:
    def __init__(self):
        self.near_points = []
        self.far_points = []
        self.calib_mode = "Near"
        self.is_calibrated = False


    def capture(self,px,py,treshold):
        if self.calib_mode == "Near":
            self.near_points.append(((px,py),treshold))
        else :
            self.far_points.append(((px,py),treshold))

        if len(self.near_points) >=4 and len(self.far_points) >=4 :
            self.is_calibrated = True

    def get_calibrated_range(self,curent_treshold):
        if not self.is_calibrated:
            return None
        avg_near_th = sum(p[1] for p in self.near_points) / len(self.near_points)
        avg_far_th = sum(p[1] for p in self.far_points) / len(self.far_points)

        deapth_ratio = np.clip((curent_treshold-avg_near_th)/(avg_far_th-avg_near_th),0,1)

        n_min_x = min(p[0][0] for p in self.near_points)
        n_max_x = max(p[0][0] for p in self.near_points)
        n_min_y = min(p[0][1] for p in self.near_points)
        n_max_y = max(p[0][1] for p in self.near_points)

        f_min_x = min(p[0][0] for p in self.far_points)
        f_max_x = max(p[0][0] for p in self.far_points)
        f_min_y = min(p[0][1] for p in self.far_points)
        f_max_y = max(p[0][1] for p in self.far_points)

        curr_min_x = n_min_x + (f_min_x - n_min_x) * deapth_ratio
        curr_max_x = n_max_x + (f_max_x - n_max_x) * deapth_ratio
        curr_min_y = n_min_y + (f_min_y - n_min_y) * deapth_ratio
        curr_max_y = n_max_y + (f_max_y - n_max_y) * deapth_ratio

        return [curr_min_x,curr_max_x], [curr_min_y,curr_max_y]

