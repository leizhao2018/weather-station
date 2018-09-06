# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:24:03 2018

@author: jmanning
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

name=['index','date','time','speed','direction','a','b','d','e','f','g','h','i','j']
df=read_csv(input_dir+weather_sta_file,names=name)
time=df['time']
speed=df['speed']
direction=df['direction']
speed1,speed2,speed3=[],[],[]
direction1,direction2,direction3=[],[],[]
for i in range(len(time)):
    if '18:18:00'<time[i]<='18:27:00':
        if direction[i]==0:
            break
        else:
            speed1.append(speed[i])
            direction1.append(math.sin(math.pi/180*direction[i]))
    if '18:27:00'<time[i]<='18:37:00':
        if direction[i]==0:
            break;
        else:
            speed2.append(speed[i])
            direction2.append(math.sin(math.pi/180*direction[i]))
    if '18:37:00'<time[i]<='18:54:00':
        if direction[i]==0:
            break;
        else:
            speed3.append(speed[i])
            direction3.append(math.sin(math.pi/180*direction[i]))
E_H_mean_speed=np.mean(speed1)
E_M_mean_speed=np.mean(speed2)
E_L_mean_speed=np.mean(speed3)
E_H_mean_direction=180/math.pi*math.asin(np.mean(direction1))
E_M_mean_direction=180/math.pi*math.asin(np.mean(direction2))
E_L_mean_direction=180/math.pi*math.asin(np.mean(direction3))
direction1,direction2,direction3=[],[],[]
speed1,speed2,speed3=[],[],[]
for i in range(len(time)):
    if '18:58:00'<time[i]<='19:03:00':
        if direction[i]==0:
            break;
        else:
            speed1.append(speed[i])
            direction1.append(math.sin(math.pi/180*direction[i]))
    if '19:03:00'<time[i]<='19:08:00':
        if direction[i]==0:
            break;
        else:
            speed2.append(speed[i])
            direction2.append(math.sin(math.pi/180*direction[i]))
    if '19:08:00'<time[i]<='19:15:00':
        if direction[i]==0:
            break;
        else:
            speed3.append(speed[i])
            direction3.append(math.sin(math.pi/180*direction[i]))
N_H_mean_speed=np.mean(speed1)
N_M_mean_speed=np.mean(speed2)
N_L_mean_speed=np.mean(speed3)
N_H_mean_direction=360+180/math.pi*math.asin(np.mean(direction1))
N_M_mean_direction=360+180/math.pi*math.asin(np.mean(direction2))
N_L_mean_direction=360+180/math.pi*math.asin(np.mean(direction3))
direction1,direction2,direction3=[],[],[]
speed1,speed2,speed3=[],[],[] 
for i in range(len(time)):
    if '19:20:00'<time[i]<='19:25:00':
        if direction[i]==0:
            break;
        else:
            speed1.append(speed[i])
            direction1.append(math.sin(math.pi/180*direction[i]))
    if '19:25:00'<time[i]<='19:30:00':
        if direction[i]==0:
            break;
        else:
            speed2.append(speed[i])
            direction2.append(math.sin(math.pi/180*direction[i]))
    if '19:30:00'<time[i]<='19:35:00':
        if direction[i]==0:
            break;
        else:
            speed3.append(speed[i]) 
            direction3.append(math.sin(math.pi/180*direction[i]))
W_H_mean_speed=np.mean(speed1)
W_M_mean_speed=np.mean(speed2)
W_L_mean_speed=np.mean(speed3)
W_H_mean_direction=360+180/math.pi*math.asin(np.mean(direction1))
W_M_mean_direction=360+180/math.pi*math.asin(np.mean(direction2))
W_L_mean_direction=360+180/math.pi*math.asin(np.mean(direction3))
direction1,direction2,direction3=[],[],[]
speed1,speed2,speed3=[],[],[] 
for i in range(len(time)):
    if '19:49:00'<time[i]<='19:54:00':
        if direction[i]==0:
            break;
        else:
            speed1.append(speed[i])
            direction1.append(math.sin(math.pi/180*direction[i]))
    if '19:54:00'<time[i]<='19:59:00':
        if direction[i]==0:
            break;
        else:
            speed2.append(speed[i])
            direction2.append(math.sin(math.pi/180*direction[i]))
    if '19:59:00'<time[i]<='20:06:00':
        if direction[i]==0:
            break;
        else:
            speed3.append(speed[i])
            direction3.append(math.sin(math.pi/180*direction[i]))
S_H_mean_speed=np.mean(speed1)
S_M_mean_speed=np.mean(speed2)
S_L_mean_speed=np.mean(speed3)
S_H_mean_direction=180-180/math.pi*math.asin(np.mean(direction1))
S_M_mean_direction=180-180/math.pi*math.asin(np.mean(direction2))
S_L_mean_direction=180-180/math.pi*math.asin(np.mean(direction3))
data={'time':time,'speed':speed,'direction':direction}
frame=DataFrame(data)        
mean_speed=[E_H_mean_speed, E_M_mean_speed, E_L_mean_speed,
            N_H_mean_speed, N_M_mean_speed, N_L_mean_speed,
            W_H_mean_speed, W_M_mean_speed, W_L_mean_speed,
            S_H_mean_speed, S_M_mean_speed, S_L_mean_speed]
mean_direction=[E_H_mean_direction, E_M_mean_direction, E_L_mean_direction,
            N_H_mean_direction, N_M_mean_direction, N_L_mean_direction,
            W_H_mean_direction, W_M_mean_direction, W_L_mean_direction,
            S_H_mean_direction, S_M_mean_direction, S_L_mean_direction]
print mean_speed
print mean_direction
