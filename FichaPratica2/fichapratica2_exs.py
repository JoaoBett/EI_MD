# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:24:46 2023

@author: João Bettencourt
"""

#%%
#EX 1
import numpy as np
import math as mt
import matplotlib.pyplot as plt

#a)
def f(x):
    out = (mt.cos(x) + (mt.e**x))
    return out

#b)
a = f(0)

b = f(mt.pi)

#c)
c = np.linspace(1, 2,98)

print(c)

##################################Fazer D e E errado
#d)
#d = f(x)
#print(D)    #x is not defined

#e)
x = np.linspace(-2, 2)

#plt.plot(x,f(x))
plt.show()

#%%
#EX 2

def g(x):
    out = ((x**5)-(3*x**4)-(3*x**3)+(7*x**2)+(6*x))
    return out

H = g(-1)

plt.plot(H)
plt.show()

#%%
#EX 3
def r(x,y):
    out = (y*((0.5)**(x/140)))
    return out
    
e = r(x,10)    

plt.plot(e)
plt.show()
#%%
#EX 4

#a)
def z(n):
    out = 0    
    return out

#b)

#%%
#EX 5

#a)




#b)






