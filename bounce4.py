# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 11:01:29 2014

@author: t08-32
"""

from visual import *
import numpy as np
from numpy import cross
from scipy.integrate import quad

def v1x(dt, g, v0, M1, M2, b, a):
    T = (M1+M2)*g[1]
    v1x = v0[0] + T*b*dt/(M1*np.sqrt(a**2+b**2)) 
    return v1x
    
def v1y(dt, g, v0, M1, M2, b, a):
    T = 1
    v1y = v0[1] + g[1]*dt - T*dt*a/(M1*np.sqrt(a**2+b**2))
    return v1y    

def v2x(dt, g, v0, M1, M2, b, a):
    T = (M1+M2)*g[1]
    v2x = v0[0] - T*dt*b/(M2*np.sqrt(a**2+b**2))
    return v2x

def v2y(dt, g, v0, M1, M2, b, a):
    T = 1
    v2y = v0[1] + g[1]*dt + T*dt*a/(M2*np.sqrt(a**2+b**2))
    return v2y
    
g = vector(0.,-10.,0.)
t = 0.

ball1 = sphere(pos=(0,12,0), radius=0.5, color=color.orange, material=materials.emissive)
ball2 = sphere(pos=(2,7,2), radius=1.0, color=color.blue, material=materials.emissive)
rod = cylinder(pos=(0,12,0), axis=(2,-5,2), radius=0.2)
wall = box(pos=(0,-0.1,0), size=(12,0.2,12), color=color.magenta, material=materials.emissive)
ball1.velocity = ball2.velocity = vector(0, 0, 0)
dt = 0.01
L = abs(ball1.pos-ball2.pos)
deltax = 0
k = vector(0.1,0.1,0.1)
M1 = ball1.radius**3
M2 = ball2.radius**3 

T = (M1+M2)*g[1]

while 1:
    
    rate (100)
    
    a = ball1.pos[1]-ball2.pos[1]
    b = abs(ball2.pos[0]-ball1.pos[0])
    
    #ball1.velocity[0] = v1x(dt, g, ball1.velocity, M1, M2, b, a)
    #ball2.velocity[0] = v2x(dt, g, ball2.velocity, M1, M2, b, a)
    ball2.velocity[1] = v2y(dt, g, ball2.velocity, M1, M2, b, a)   
    
    ball1.pos[0] = ball1.pos[0] + quad(v1x,0,dt,args=(g, ball1.velocity, M1, M2, b, a))[0]
    ball1.pos[1] = ball1.pos[1] + quad(v1y,0,dt,args=(g, ball1.velocity, M1, M2, b, a))[0]
    #ball1.pos[1] = ball1.pos[1] - ball1.velocity[1]*dt - 0.5*g[1]*dt**2 + 0.5*T*dt**2*a/(M1*np.sqrt(a**2+b**2))
    
    ball2.pos[0] = ball2.pos[0] + quad(v2x,0,dt,args=(g, ball2.velocity, M1, M2, b, a))[0]
    ball2.pos[1] = ball2.pos[1] + quad(v2y,0,dt,args=(g, ball1.velocity, M1, M2, b, a))[0]
    #ball2.pos[1] = ball2.pos[1] - ball2.velocity[1]*dt - 0.5*g[1]*dt**2 - 0.5*T*dt**2*a/(M2*np.sqrt(a**2+b**2))   
    
    if ball1.pos[1]<ball1.radius:
        c = (np.random.random(),np.random.random(),np.random.random())
        wall.color = c
        ball1.velocity[1] = -ball1.velocity[1]

    if ball2.pos[1]<ball2.radius:
        ball2.velocity[1] = -ball2.velocity[1]
        
    rod.pos = ball1.pos
    rod.axis = ball2.pos - ball1.pos
    deltax = abs(ball1.pos-ball2.pos) - L
    
    r1, r2 = ball1.pos, ball2.pos
    M = r1.cross(ball1.velocity) + r2.cross(ball2.velocity)
    print M