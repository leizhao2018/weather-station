# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:52:26 2018
Caculate the average of the direction and speed about the weather station

@author: leizhao
"""

import numpy as np
#from pandas import DataFrame
from pandas import read_csv
import math
import matplotlib.pyplot as plt
#########################
#HARDCODES
input_dir='/home/jmanning/leizhao/data_file/'
output_dir='/home/jmanning/leizhao/picture/'
weather_sta_file='weather-station-output180912.txt'  #test data about weather_station
test_times_file='time_remove_fan.txt'
index=[0,1,2,4,5,7,9,10,11,13,14,15]  #Index of the time interval to which output is required
###########################
MT_name=['M_date']
tm=read_csv(input_dir+test_times_file,names=MT_name)
t_times=tm.icol(0)
#times=['14:54:00','14:59:00','15:04:00','15:09:00','15:13:00','15:18:00','15:23:00',
#'15:24:00','15:29:00','15:36:00','15:41:00','15:46:00','15:51:00','15:54:00','15:59:00','16:04:00','16:04:00']
#times present the time that remove the location of fan or switch the speed of fan
name=['index','date','time','speed','direction','a','b','d','e','f','g','h','i','j']
df=read_csv(input_dir+weather_sta_file,names=name)
time=df['time']
speed=df['speed']
direction=df['direction']
u,v,uu,vv,mean_speed,mean_direction=[],[],[],[],[],[]
for  j in index:
    ss_direction1,ss_direction2=[],[]
    for i in range(len(time)):
            if t_times[j]<time[i]<=t_times[j+1]:
                if direction[i]==0:
                   break
                else:
                    ss_direction1.append(speed[i]*math.cos(math.pi/180*direction[i]))
                    ss_direction2.append(speed[i]*math.sin(math.pi/180*direction[i]))
    s=np.sqrt((np.square(np.mean(ss_direction1))+np.square(np.mean(ss_direction2))))
    mean_speed.append(s)
    if np.mean(ss_direction1)>0 and np.mean(ss_direction2)>0:
        mean_direction.append(180/math.pi*math.asin(np.mean(ss_direction2)/s))
    elif np.mean(ss_direction1)<0 and np.mean(ss_direction2)>0:
        mean_direction.append(180/math.pi*math.acos(np.mean(ss_direction1)/s))
    elif np.mean(ss_direction1)<0 and np.mean(ss_direction2)<0:
        mean_direction.append(180+180/math.pi*math.acos(abs(np.mean(ss_direction1)/s)))
    else:
        mean_direction.append(360-180/math.pi*math.acos(abs(np.mean(ss_direction1)/s)))  
    u.append(np.mean(ss_direction1))
    v.append(np.mean(ss_direction2))
uu=np.array(u).reshape(4,3)
vv=np.array(v).reshape(4,3)
s=np.array(mean_speed).reshape(4,3)
x, y = np.meshgrid(np.arange(0.1, 1.5 , .5), np.arange(0.1,2.0,.5))
plt.figure()
plt.title('speed with "H M L" and direction with "E W S N"')
Q = plt.quiver(x, y, vv*s, uu*s, units='height')  #the angle connection of compass(a1) and math(a2):a2=(np.pi-a1)+k*360
qk = plt.quiverkey(Q, 0.91 ,0.9, 2, r'$direction E$', labelpos='N',
                   coordinates='figure')
plt.savefig(output_dir+'speed with "H M L" and direction with "E W S N".png')
