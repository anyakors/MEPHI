# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 00:10:09 2014

@author: User
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


a=0.
b=1.
N=100
d=10
epsilon=0.9
x = y = np.linspace(a, b, num=N)
XX, YY = np.meshgrid(x,y)


Z = np.zeros(XX.size).reshape(N,N)
Z[(N-5*d)/2:(N+5*d)/2,(N-d)/2]=-100.
Z[(N-5*d)/2:(N+5*d)/2,(N+d)/2]=100.

s = x.size

norm = np.linalg.norm(Z)
delta = 1.

while abs(norm-delta)> epsilon:
    Z[1:-1,1:-1]=(1/4.)*(Z[1:-1,2:]+Z[1:-1,:-2]+Z[2:,1:-1]+Z[:-2,1:-1])
    Z[(N-5*d)/2:(N+5*d)/2,(N-d)/2]=-100.
    Z[(N-5*d)/2:(N+5*d)/2,(N+d)/2]=100.
    delta = norm
    norm=np.linalg.norm(Z)
    print abs(norm-delta)                          

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
print XX.shape, YY.shape, Z.shape
ax.plot_surface(XX, YY, Z, rstride=1, cstride=1,cmap=cm.jet, linewidth=0, antialiased=False)
plt.savefig ("3D")


plt.show()