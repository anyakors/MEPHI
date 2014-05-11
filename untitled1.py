# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:08:06 2014

@author: t08-32
"""

import numpy as np

Z = np.random.randn(5)
print Z
Z[1:-1]=(1/2.)*(Z[2:]+Z[:-2])
print Z