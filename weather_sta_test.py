# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:52:26 2018
get the data of weather station test
caculate the average of direction and speed
output the picture with direction and speed
@author: leizhao
"""

import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
import zlconversions as zl

#########################
#HARDCODES
input_dir='/home/jmanning/leizhao/data_file/input_data/'
output_dir='/home/jmanning/leizhao/data_file/output_data/picture/'
weather_sta_file='weatherstation180912.txt' # explain where this inputfile came from
Date=['Sep 12,2018']      #Data is the weather station test date in the United Station
test_times_file='time_remove_fan.txt'
index=[0,1,2,4,5,7,9,10,11,13,14,15]  #Index of the time interval to which output is required
###########################
MT_name=['D_from','M_date'] # column names in the test_time_file is direction from and moment time
tm=read_csv(input_dir+test_times_file,names=MT_name)  #get the data 
t_times=tm['M_date'] #moment time that move fan
F_from=tm['D_from']  #the wind from
#times present the time that remove the location of fan or switch the speed of fan
name=['index','date','time','speed','direction','a','b','d','e','f','g','h','i','j']  #set the header for weatherstation180912.txt
df=read_csv(input_dir+weather_sta_file,names=name) # the data saved by the weather_plots2.py program
time_df=df['time']  
speed_df=df['speed']
direction_df=df['direction']
u,v,mean_speed,mean_direction=[],[],[],[]
s,d=[],[] #s,d present the speed and direction
for  j in index: # for each of the x * y settings (x speeds at each of the y directions)
    mean_u,mean_v,mean_interval_u,mean_interval_v,m_speed=[],[],[],[],[] # "mean_interval_u" and "mean_interval_v" is are the values for one of the x * y settings
    for i in range(len(time_df)):
            if t_times[j]<time_df[i]<=t_times[j+1]:#t_time reprensent the moment that mov the fan
                if speed_df[i]==0: #exclude the data that has't the speed data
                   break
                else:
                    [u_t,v_t]=zl.sd2uv(speed_df[i],direction_df[i])  #chang the spped and direction to the u,v
                    mean_interval_u.append(u_t)  
                    mean_interval_v.append(v_t)
    mean_u.append(np.mean(mean_interval_u))  #calculate the average of u in interval
    mean_v.append(np.mean(mean_interval_v))  #calculate the average of v in interval
#make the numpy of u and v
    u.append(mean_u[0])   
    v.append(mean_v[0])
u=np.array(u).reshape(4,3)
v=np.array(v).reshape(4,3)
x, y = np.meshgrid(np.arange(0.31, 1 , .3), np.arange(0.25,1.2,.25))
fig=plt.figure()
fig.suptitle('Weather station test '+Date[0]+' result',fontsize=14)
ax=fig.add_subplot(111)
Q=ax.quiver(x, y, -u, -v, units='height')  #the angle connection of compass(a1) and math(a2):a2=(np.pi-a1)+k*360
ax.quiverkey(Q, 0.87 ,0.9, 2, 'direction 2 m/s', labelpos='W', coordinates='figure')
ax.annotate(s=F_from[index[0]],xy=(0.2,0.25))
ax.annotate(s=F_from[index[3]],xy=(0.2,0.5))
ax.annotate(s=F_from[index[6]],xy=(0.2,0.75))
ax.annotate(s=F_from[index[9]],xy=(0.2,1.0))
ax.annotate(s='H',xy=(.31,0.05))
ax.annotate(s='M',xy=(.61,0.05))
ax.annotate(s='L',xy=(.91,0.05))
ax.set_xlim(0.15,1)
ax.set_ylim(0,1.2)
ax.set_ylabel('direction',fontsize=12)
ax.set_xlabel('fan speed',fontsize=12)
plt.xticks([])
plt.yticks([])
plt.savefig(output_dir+'Weather station test'+Date[0]+'.png',dpi=300)
