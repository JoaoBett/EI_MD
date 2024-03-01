# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 08:16:24 2023

@author: João Bettencourt
"""
import math as mt
#Exs
#5
#a)
A=set(range(3,101,3))

B=set(x for x in range(66,141) if x%7 == 0)

#b)
C = A^B

print(len((A.union(C)).intersection(B)))


#6
#a)

D = set(y for y in range(1,411) if y%2==0 and y/7!=0)

#b)

E = set(z for z in range(1,411) if mt.sqrt(z)**2 == z)

#c)

F = set(k for k in range(1,411) if k/3!=0 and mt.sqrt(k)**2 != k)