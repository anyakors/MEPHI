# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 08:47:30 2014

@author: t08-32
"""

from visual import *
import numpy as np

g = vector(0.,-10.,0.)
t = 0.

ball1 = sphere(pos=(0,12,0), radius=0.5, color=color.orange, material=materials.emissive)
ball2 = sphere(pos=(2,7,2), radius=1.0, color=color.blue, material=materials.emissive)
rod = cylinder(pos=(0,12,0), axis=(2,-5,2), radius=0.2)
wall = box(pos=(0,-0.1,0), size=(12,0.2,12), color=color.magenta, material=materials.emissive)
ball1.velocity = ball2.velocity = vector(0, 0, 0)
dt = 0.005
L = abs(ball1.pos-ball2.pos)
deltax = 0
k = vector(0.1,0.1,0.1)
M1 = ball1.radius**3
M2 = ball2.radius**3 

while 1:
    
    rate (100)
    
    ball1.velocity = ball1.velocity + g*dt - k*deltax/M1 
    ball2.velocity = ball2.velocity + g*dt - k*deltax/M2
    
    ball1.pos = ball1.pos + ball1.velocity*dt
    ball2.pos = ball2.pos + ball2.velocity*dt
    
    if ball1.pos[1]<ball1.radius:
        c = (np.random.random(),np.random.random(),np.random.random())
        wall.color = c
        ball1.velocity.y = -ball1.velocity.y

    if ball2.pos[1]<ball2.radius:
        ball2.velocity.y = -ball2.velocity.y
        
    rod.pos = ball1.pos
    rod.axis = ball2.pos - ball1.pos
    deltax = abs(ball1.pos-ball2.pos) - L