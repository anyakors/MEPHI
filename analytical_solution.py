# -*- coding: utf-8 -*-
"""
Created on Sat Mar 01 10:18:53 2014

@author: t08-32
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def solution(x,y,k):
    l=1.
    return (400./pi)*sin(pi*k*x/l)*sinh(pi*k*y/l)/sinh(pi*k)/k

a=0.
b=1.
N=100
delta = (b-a)/N
x = y = np.linspace(a, b, num=N)
XX, YY =np.meshgrid(x,y)
Z=np.zeros(XX.size).reshape(N,N)
print Z
for i in range(0,x.size):
    for j in range(0,x.size):
        for n in range(1,N/2,2):
            Z[i,j]=Z[i,j]+solution(XX[i,j],YY[i,j],n)
            


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(XX, YY, Z, rstride=1, cstride=1,cmap=cm.jet, linewidth=0, antialiased=False)
plt.savefig ("3D")


plt.show()
        
