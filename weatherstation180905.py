# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:24:03 2018

@author: leizhao 
"""

import numpy as np
from pandas import DataFrame
from pandas import read_csv
import math
#########################
#HARDCODES
input_dir='/home/jmanning/leizhao/'
###########################
weather_sta_file='weatherstation180905.txt'
times=['18:18:00','18:27:00','18:37:00','18:54:00','18:58:00','19:03:00','19:08:00',
'19:15:00','19:20:00','19:25:00','19:30:00','19:35:00','19:49:00','19:54:00','19:59:00','20:06:00']
name=['index','date','time','speed','direction','a','b','d','e','f','g','h','i','j']
df=read_csv(input_dir+weather_sta_file,names=name)
time=df['time']
speed=df['speed']
direction=df['direction']
mean_speed=[]
mean_direction=[]
j=0
while j<=15:
    print j
    m_speed=[]
    s_direction=[]
    for i in range(len(time)):
            if times[j]<time[i]<=times[j+1]:
                if direction[i]==0:
                   break
                else:
                  m_speed.append(speed[i])
                  s_direction.append(math.sin(math.pi/180*direction[i]))
    mean_speed.append(np.mean(m_speed))
    mean_direction.append(180/math.pi*math.asin(np.mean(s_direction)))
    j+=1
print mean_speed
print mean_direction
