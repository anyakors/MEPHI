# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 10:31:09 2014

@author: t08-32
"""

from visual import *
import numpy as np
from numpy import cross
from scipy.integrate import quad


g = vector(0.,-10.,0.)
t = 0.

rod = cylinder(pos=(0,12,0), axis=(2,5,2), radius=0.2)
wall = box(pos=(0,-0.1,0), size=(12,0.2,12), color=color.magenta, material=materials.emissive)

dt = 0.01
L = abs(np.linalg.norm(cylinder.pos-cylinder.axis))
deltax = 0

k = vector(0.1,0.1,0.1)
n = vector(0,1.,0)
Rc = cylinder.pos + 0.5*cylinder.axis
Rp = cylinder.pos + cylinder.axis
Rcp = Rp - Rc
m = 1
e = 0.8
n = vector(0,0,1)

T = m*g

while 1:
    
    rate (100)
    
    j = -(1+e)*dot(rod.velocity,n)/(1 + (12*Rcp[0]**2)/L**2)
    
    if (rod.pos[1]+rod.axis[1])<rod.radius:
        rod.axis.rotate(angle=1,axis=,origin=rod.axis)
        rod.velocity[1] += j
    
    if rod.pos[1]<rod.radius:
        rod.velocity[1] = rod.velocity[1] + j
    
    r1, r2 = ball1.pos, ball2.pos
    M = r1.cross(ball1.velocity) + r2.cross(ball2.velocity)
    print M