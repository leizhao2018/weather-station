# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:52:26 2018
Caculate the average of the direction and speed about the weather station

@author: leizhao
"""

import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
import zlconvertions as zl

#########################
#HARDCODES
input_dir='/home/jmanning/leizhao/data_file/'
output_dir='/home/jmanning/leizhao/picture/'
weather_sta_file='weather-station-output180912.txt' # explain where this inputfile came from
Date=['Sep 12,2018']      #Data is the weather station test date in the United Station
test_times_file='time_remove_fan.txt'
index=[0,1,2,4,5,7,9,10,11,13,14,15]  #Index of the time interval to which output is required
###########################
MT_name=['D_from','M_date'] # column names in the test_time_file
tm=read_csv(input_dir+test_times_file,names=MT_name)
t_times=tm['M_date']
F_from=tm['D_from']
#times=['14:54:00','14:59:00','15:04:00','15:09:00','15:13:00','15:18:00','15:23:00',
#'15:24:00','15:29:00','15:36:00','15:41:00','15:46:00','15:51:00','15:54:00','15:59:00','16:04:00','16:04:00']
#times present the time that remove the location of fan or switch the speed of fan
name=['index','date','time','speed','direction','a','b','d','e','f','g','h','i','j']
df=read_csv(input_dir+weather_sta_file,names=name) # this reads data saved by the weather_plots2.py program?
time=df['time']
speed=df['speed']
direction=df['direction']
u,v,uu,vv,mean_speed,mean_direction=[],[],[],[],[],[] # where "u" is a list of x*y eastward flows and "uu" is reshaped list
ss_direction=[]
ss,dd=[],[]
for  j in index: # for each of the x * y settings (x speeds at each of the y directions)
    mean_u,mean_v,u1,v1,m_speed=[],[],[],[],[] # where "u1" and "v1" are the values for one of the x * y settings
    for i in range(len(time)):
            if t_times[j]<time[i]<=t_times[j+1]:
                if direction[i]==0: #why do you not include direction=0?
                   break
                else:
                    [u1_t,v1_t]=zl.sd2uv(speed[i],direction[i])
                    u1.append(u1_t)
                    v1.append(v1_t)
    mean_u.append(np.mean(u1))
    mean_v.append(np.mean(v1))
    u.append(mean_u[0])
    v.append(mean_v[0])
    [s_t,d_t]=zl.uv2sd(mean_u[0],mean_v[0])
    ss.append(s_t)
    dd.append(d_t)
uu=np.array(u).reshape(4,3)
vv=np.array(v).reshape(4,3)
s=np.array(ss).reshape(4,3)
d=np.array(dd).reshape(4,3)
x, y = np.meshgrid(np.arange(0.15, 1.6 , .5), np.arange(0.19,1.8,.5))
plt.figure()
plt.title('Weather station test '+Date[0]+' result on speed and direction',fontsize=10)
#for i in range(4):
#    if d[i][0]<315 and  d[i][0]>=225:
#        plt.annotate(s='W',xy=(0.02,0.15+0.5*i))
#    elif d[i][0]<225 and d[i][0]>=135:
#        plt.annotate(s='S',xy=(0.02,0.15+0.5*i))
#    elif d[i][0]<135 and d[i][0]>=45:
#        plt.annotate(s='E',xy=(0.02,0.15+0.5*i))
#    else:
#        plt.annotate(s='N',xy=(0.02,0.15+0.5*i))
plt.annotate(s='H',xy=(0.11,0.05))
plt.annotate(s='M',xy=(0.61,0.05))
plt.annotate(s='L',xy=(1.11,0.05))
plt.annotate(s=F_from[index[0]],xy=(0.02,0.15))
plt.annotate(s=F_from[index[3]],xy=(0.02,0.65))
plt.annotate(s=F_from[index[6]],xy=(0.02,1.15))
plt.annotate(s=F_from[index[9]],xy=(0.02,1.65))
plt.ylabel('Direction From')
plt.xlabel('Fan Speed')
# In order to get the arrows to point in the right direction, we multiply u & v by -1.0 
Q = plt.quiver(x, y, -uu, -vv, units='height')  #the angle connection of compass(a1) and math(a2):a2=(np.pi-a1)+k*360
#qk = plt.quiverkey(Q, 0.87 ,0.91, 2, r'$direction W$', labelpos='N', coordinates='figure')# why is this commented out?
plt.xticks([])
plt.yticks([])
plt.savefig(output_dir+'Weather station test '+Date[0]+' result on speed and direction.png',bbox_inches='tight')
