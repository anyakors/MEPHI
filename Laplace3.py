# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 21:24:52 2014

@author: User
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

pi=np.pi
a=0.
b=2.
R1=0.5
R2=1.
N=1000
d=(b-a)/N
epsilon=0.9
r=np.linspace(a,b,num=N)


Z = np.zeros(r.size).reshape(N)
Z[int(R1/d)]=-100.
Z[int(R2/d)]=100.

s = r.size

norm = np.linalg.norm(Z)
delta = 1.

while abs(norm-delta)> epsilon:
    Z[1:-1]=(1/2.)*(Z[2:]+Z[:-2])
    Z[int(R1/d)]=-100.
    Z[int(R2/d)]=100.
    delta = norm
    norm=np.linalg.norm(Z)
    print abs(norm-delta)                          

plt.plot(r,Z)
plt.show()
