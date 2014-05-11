# -*- coding: utf-8 -*-
"""
Created on Sun May 11 12:12:35 2014

@author: t08-32
"""

import numpy as np

global a = 0 
global b = 1 

def density(x):
    density = 1/(4*np.pi)
    return density
    
def Fi(x,N):
    Fi = 
    for j in range(0,N):
        Fi(j) = x*(-1)**j + (b-a)*j/N
    return Fi