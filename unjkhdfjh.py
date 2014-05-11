# -*- coding: utf-8 -*-
"""
Created on Sun May 11 09:55:20 2014

@author: t08-32
"""


from visual import *
import numpy as np
from numpy import cross
from scipy.integrate import quad

rod = cylinder(pos=(0,12,0), axis=(2,-5,2), radius=0.2)

    
rod.rotate(angle=pi/2, axis=(0,0,1), origin=(0,12,5))