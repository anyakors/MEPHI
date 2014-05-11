# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 21:24:52 2014

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def Trace(A):
    #A is the list of lists
    Tr = 0
    for i in range(len(A)):    
        Tr = Tr + A[i][i]
    return abs(Tr)

a=0.
b=1.
N=100
epsilon=0.1
#x = y = range(a*N, b*N, int((b-a)/N))
x = y = [float(j) for j in range(N)]

#s = x.size

U = [[0 for x in xrange(N)] for x in xrange(N)] 
U[0][:] = [100. for i in xrange(N)]

Tr = Trace(U)
delta=0.

while(Tr-delta) > epsilon:
    for i in range(1,len(U)-1):
        for j in range(1,len(U)-1):
            U[i][j]=(1/4.)*(U[i+1][j]+U[i-1][j]+U[i][j+1]+U[i][j-1])
    delta = Tr
    Tr = Trace(U)
    print Tr-delta
    
    
#print U
#print Z            

z = np.linspace(a, b, num=N)
XX, YY = np.meshgrid(z,z)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(XX, YY, U, rstride=1, cstride=1,cmap=cm.jet, linewidth=0, antialiased=False)
plt.savefig ("3D")


plt.show()
        