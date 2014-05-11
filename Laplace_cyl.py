# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 00:10:09 2014

@author: User
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def PolCart(r,theta):
    import numpy as np                                                                  
    X = r*np.cos(theta)                                                             
    Y = r*np.sin(theta)                                                             
    return X,Y

a = 0.
R2 = 1.
R1 = 0.3
N = 100
dth = 360./N
dr = (2*R2-a)/N

epsilon = 0.1
x = np.arange(0.,360.0,dth)

theta = (np.pi/180.0 )*x
r = np.arange(a,2*R2,dr)
print r.shape

Z = np.zeros((N,N))
Z[int(R1/dr),:] = -100.
Z[int(R2/dr),:] = 100.

#s = x.size

norm = np.linalg.norm(Z)
delta = 1.

while abs(norm-delta)> epsilon:
    Z[1:-1,1:-1]=(1/4.)*(Z[1:-1,2:]+Z[1:-1,:-2]+Z[2:,1:-1]+Z[:-2,1:-1])
    Z[int(R1/dr),:] = -100.
    Z[int(R2/dr),:] = 100.
    delta = norm
    norm=np.linalg.norm(Z)
    print abs(norm-delta)                          

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
X,Y = PolCart(r,theta)
XX,YY = np.meshgrid(X,Y)
print r.shape, theta.shape
ax.plot_surface(XX, YY, Z, rstride=1, cstride=1,cmap=cm.jet, linewidth=0, antialiased=False)
plt.savefig ("3D")


plt.show()