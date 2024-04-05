# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:37:50 2024

@author: joaog
"""
import math as mt
import numpy as np

U = np.arange(1,5001,1)

U1 = []
for x in U:
  if x % 5 != 0 and x % 2 != 0:
      U1.append(x)
      
U2 = []
for x in U:
    if x % 6 == 0 and x % 15 == 0:
        U2.append(x)
        
        