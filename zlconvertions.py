# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:08:40 2018

@author: jmanning
"""
import numpy as np
import math
    
def sd2uv(s,d):
    """transform the speed and direction data to the x,y components of the arrow vectors(u,v)""" 
    u_t=math.sin(math.radians(d))
    v_t=math.cos(math.radians(d))
    if abs(u_t)==1:
        v=0
        u=float(s)*u_t
    elif abs(v_t)==1:
        u=0
        v=float(s)*v_t
    else:
        u=float(s)*u_t
        v=float(s)*v_t
    return u,v

def uv2sd(u,v):
    """transform the x,y components of the arrow vectors(u,v) to the speed and direction data"""
#    s=math.sqrt(u**2+v**2)
    s=math.sqrt(np.square(u)+np.square(v))
    if s==0:
        d=0
    else:
        if abs(v/s)==1:
            d=180/np.pi*math.acos(float(v/s))
        elif abs(u/s)==1:
            d=180/np.pi*math.asin(float(u/s))
        else:
            dt=180/np.pi*math.atan(float(u/v))
            if u>0 and v>0:
                d=dt
            elif v<0:
                d=180+dt
            else:
                d=360+dt
    return s,d