import math
import numpy as np

class smoother :
    def __init__(self,min_alpha=0.05,max_alpha=0.9,dead_zone=2):
        self.prex_x,self.prex_y = 0,0
        self.dead_zone = dead_zone
        self.min_alpha = min_alpha
        self.max_alpha = max_alpha

    def smooth(self,cur_x,cur_y):
        if cur_x is  None or cur_y is  None:
            return None,None,self.min_alpha,None
        velocity = math.hypot(cur_x-self.prex_x,cur_y-self.prex_y)

        if velocity < self.dead_zone:
            return int(self.prex_x),int(self.prex_y),self.min_alpha,True


        dynamic_alpha = np.interp(velocity,[0,50],[self.min_alpha,self.max_alpha])

        smooth_x = ( dynamic_alpha * cur_x) + ((1- dynamic_alpha)* self.prex_x)
        smooth_y = ( dynamic_alpha * cur_y) + ((1- dynamic_alpha)* self.prex_y)

        self.prex_x,self.prex_y = smooth_x,smooth_y

        return int(smooth_x),int(smooth_y),dynamic_alpha,False

