# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 08:47:30 2014

@author: t08-32
"""

from visual import *
import numpy as np

g = vector(0.,-10.,0.)
t = 0.

ball = sphere(pos=(0,12,0), radius=0.5, color=color.orange, material=materials.emissive)
wall = box(pos=(0,-0.1,0), size=(12,0.2,12), color=color.magenta, material=materials.emissive)
ball.velocity = vector(0, 0, 0)
dt = 0.01

while 1:
    rate (100)
    ball.velocity = ball.velocity + g*dt
    ball.pos = ball.pos + ball.velocity*dt
    if ball.pos[1]<ball.radius:
        c = (np.random.random(),np.random.random(),np.random.random())
        wall.color = c
        ball.velocity.y = -ball.velocity.y