from functools import reduce
import numpy as np
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from scipy.stats import norm
from scipy.stats import multivariate_normal

data=cv2.imread(r'C:\\Users\\Nitesh\\Desktop\\test_img.jpeg',0)

ret, thresh = cv2.threshold(data, 60,255, cv2.THRESH_BINARY)

heat_map=np.zeros((500,500),dtype=np.uint8)
curr_x=0
curr_y=0
x=0
y=0
z_vals=[]
while(x<500):
    while(y<500):
        X = np.linspace(x,x+50,50)
        Y = np.linspace(y,y+50,50)
        X, Y = np.meshgrid(X,Y)

        pos = np.empty(X.shape+(2,))
        pos[:,:,0]=X
        pos[:,:,1]=Y

        max_val=np.sum(thresh[y:y+50,x:x+50])
        non_zero_y,non_zero_x=np.where(thresh[y:y+50,x:x+50]>50)

        mean_x=x
        mean_y=y
        std_x=1
        std_y=1
        if(len(non_zero_x)):
            mean_x+=non_zero_x.mean()
            std_x=non_zero_x.std()
        else:
            mean_x+=25

        if(len(non_zero_y)):
            mean_y+=non_zero_y.mean()
            std_y=non_zero_y.std()
        else:
            mean_y+=25

        if(std_x==0):
            std_x=1
        if(std_y==0):
            std_y=1

        try:
            z=multivariate_normal([mean_x, mean_y],[[std_x, 0], [0, std_y]])
        except Exception as e:
            print("std_x: ",std_x," std_y: ",std_y," non_zero_x: ",non_zero_x," non_zero_y: ",non_zero_y)
        y+=50
        curr_y+=1

        temp=z.pdf(pos)
        z_vals.append(temp)
        a=z_vals

    x+=50
    curr_x+=1
    curr_y=0
    y=0

fig=plt.figure()
ax = fig.gca(projection='3d')
X = np.linspace(0,500,500)
Y = np.linspace(0,500,500)
X, Y = np.meshgrid(X,Y)
print(X.shape)
pos = np.empty(X.shape+(2,))
pos[:,:,0]=X
pos[:,:,1]=Y
z_vals=np.array(z_vals)
z_vals=z_vals.reshape(500,500)
print(z_vals.shape)
ax.plot_surface(X, Y, z_vals, cmap="plasma")

plt.show()
