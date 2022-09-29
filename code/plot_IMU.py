import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import csv
import time
import os
from IPython import display
import matplotlib.animation as animation

N = 50  # number of points to keep

# Variables to plot
proc1 = np.full(shape=(N,), fill_value=np.nan)
proc2 = np.full(shape=(N,), fill_value=np.nan)
proc3 = np.full(shape=(N,), fill_value=np.nan)
proc4 = np.full(shape=(N,), fill_value=np.nan)
proc5 = np.full(shape=(N,), fill_value=np.nan)
proc6 = np.full(shape=(N,), fill_value=np.nan)

fig, (ax, ay, az, wx, wy, wz) = plt.subplots(6, 1)

line1, = ax.plot(proc1, 'r-')
line2, = ay.plot(proc2, 'g-')
line3, = az.plot(proc3, 'b-')
line4, = wx.plot(proc4, 'm-')
line5, = wy.plot(proc5, 'y-')
line6, = wz.plot(proc6, 'c-')

# Set scales accordingly
# ax.set_ylim(-.1, .1)
ax.set_xlim(0, N)
ax.set_xlabel('t')
ax.set_ylabel('ax')

# ay.set_ylim(-.5, .5)
ay.set_xlim(0, N)
ay.set_xlabel('t')
ay.set_ylabel('ay')

# az.set_ylim(-.1, .1)
az.set_xlim(0, N)
az.set_xlabel('t')
az.set_ylabel('az')

# wx.set_ylim(-.1, .1)
wx.set_xlim(0, N)
wx.set_xlabel('t')
wx.set_ylabel('wx')

# wy.set_ylim(-.1, .1)
wy.set_xlim(0, N)
wy.set_xlabel('t')
wy.set_ylabel('wy')

wz.set_ylim(-.1, .1)
wz.set_xlim(0, N)
wz.set_xlabel('t')
wz.set_ylabel('wz')

current_accels=[]
current_ang_accels=[]
accel_x=0
accel_y=0
accel_z=0

gyro_x=0
gyro_y=0
gyro_z=0

count=0
file=open(r"C:\\Users\\Nitesh\\Desktop\\imu_values_2_5.txt",'r')
f=file.readlines()
filename=''
filepath=r"C:\Users\Nitesh\Desktop\imu_dir"
def animate(i):
    print(i)
    global count
    count+=1
    first=True
    global f,filename
    filename=str(i)+'imu_plot.png'
    data=f[i]
    data=data[1:-1]
    accel_val=data.split(',')[0][:-1]
    gyro_val=data.split(',')[1][2:-1]
    
    accel_list=accel_val.split(' ')
    accel_list=[float(x) for x in accel_list if x!='' and x!=' ']
    accel_x=accel_list[0]
    accel_y=accel_list[1]
    accel_z=accel_list[2]
    # print(accel_x)

    gyro_list=gyro_val.split(' ')
    gyro_list=[float(x) for x in gyro_list if x!='' and x!=' ']
    gyro_x=gyro_list[0]
    gyro_y=gyro_list[1]
    gyro_z=gyro_list[2]
    # Shift all vals by one
    # Append new val to end- fetched from csv
    proc1[:-1] = proc1[1:]
    proc2[:-1] = proc2[1:]
    proc3[:-1] = proc3[1:]
    proc4[:-1] = proc4[1:]
    proc5[:-1] = proc5[1:]
    proc6[:-1] = proc6[1:]
    
    proc1[-1],proc2[-1],proc3[-1]=accel_x,accel_y,accel_z
    proc4[-1],proc5[-1],proc6[-1]=gyro_x,gyro_y,gyro_z
    line1.set_ydata(proc1)
    line2.set_ydata(proc2)
    line3.set_ydata(proc3)
    line4.set_ydata(proc4)
    line5.set_ydata(proc5)
    line6.set_ydata(proc6)
    return line1,line2,line3,line4,line5,line6,
    # plt.savefig(os.path.join(filepath,filename))
    # plt.clf()


if __name__=="__main__":
    ani = FuncAnimation(fig, animate, interval=1,frames=17004)
    writer=animation.FFMpegWriter(fps=120)
    ani.save(os.path.join(filepath,'imu_val_plot.mp4'),writer=writer)
    plt.close()
    print(count)
    # plt.show()
    # plt.savefig(os.path.join(filepath,filename))
    # plt.clf()