# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 11:01:29 2014

@author: t08-32
"""

from visual import *
import numpy as np
from scipy.integrate import quad
    
g = vector(0.,-10.,0.)
t = 0.

rod = cylinder(pos=(0,12,0), axis=(2,-5,2), radius=0.2)
wall = box(pos=(0,-0.1,0), size=(12,0.2,12), color=color.magenta, material=materials.emissive)
dt = 0.01
L = abs(rod.axis) #rod length
deltax = 0
k = vector(0.1,0.1,0.1)
M = 1 #rod mass

rod.velocity = vector(0, 0, 0)
n = vector(0,1,0) #norm vector to the wall
I = M*L**2/12
omega = vector(0,0,0)
rot_ax = vector(0,0,1) #rotation axis

while 1:
    
    rate (100)
    
    C = rod.pos + rod.axis/2    
    
    #impulse parameter
    j = -2*dot(rod.velocity,n)/(1/M + dot(C.cross(n),C.cross(n))/I)

    rp = rod.pos + rod.axis    
    omega += j*rp.cross(n)/I
    
    rod.velocity += j*n/M + 0.5*g*dt**2
    
    rod.pos = rod.pos + rod.velocity*dt
    
    #print omega*dt, rot_ax, C
    rod.rotate(angle=omega[2]*dt, axis=rot_ax, origin=C)
    