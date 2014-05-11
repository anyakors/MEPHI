# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 21:24:52 2014

@author: User
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


a=0.
b=1.
N=100
epsilon=0.1
x = y = np.linspace(a, b, num=N)
XX, YY =np.meshgrid(x,y)

Z=np.zeros(XX.size).reshape(N,N)
Z[0,0:]=100.

s=x.size

U=np.zeros(XX.size).reshape(N,N)
U[0,0:]=100.

norm=np.sqrt(np.dot(U,U).sum())
delta=0.

while(norm-delta)> N*epsilon:
    for i in range(1,s-1):
        for j in range(1,s-1):
            U[i,j]=(1/4.)*(Z[i+1,j]+Z[i-1,j]+Z[i,j+1]+Z[i,j-1])
    Z=U
    delta = norm
    norm=np.sqrt(np.dot(U,U).sum())
    print norm-delta

    
#print U
#print Z            


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(XX, YY, Z, rstride=1, cstride=1,cmap=cm.jet, linewidth=0, antialiased=False)
plt.savefig ("3D")


plt.show()
        