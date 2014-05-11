# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 08:41:29 2014

@author: t08-32
"""

from visual import *


ball = sphere(pos=(0,5,0), radius=0.5, color=color.orange, material=materials.emissive)
wall = box(pos=(0,-6,0), size=(12,0.2,12), color=color.magenta, material=materials.emissive)

print wall.size[1]