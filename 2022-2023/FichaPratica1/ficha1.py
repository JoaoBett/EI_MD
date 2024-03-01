# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:08:46 2023

@author: João Bettencourt
"""
import math as mt


#%%
#EX1

a = (35.6 * 64 - 7**3) / (45 + 5**2) 
                      
print(a)

b = 5/7 * 4 * 6**2 - (3**7/(9**3 - 236))

print(b)

c = ((3**2) * (mt.log10(76)))/(7**3 + 54) + (910**(1/3))

print(c)

d = mt.cos(5 * mt.pi/6)**2 * mt.sin(((7 * mt.pi)/8)**2) + (mt.tan((mt.pi/6) * mt.log(8))/ mt.sqrt(7))

print(d)

#%%
#EX 2

x = 13.5

y = (x**3) - (2 * x) + (23.5 * (x**2))

print (y)

w = (mt.sqrt(14 * x**3)) / (mt.e**(3*x)) 

print (w)

z = mt.log10(abs((x**2)  - (x**3)))

print (z)

#%%
#EX 3
#f = a
f = 15.62

#g = b
g = -7.08

#h = c
h = 62.5

#i = d
i = 0.5*((f * g) - h)

res = f+((f*g)/h)*(((f+i)**2)/(mt.sqrt(abs(f*g))))

print (res)


#%%

#TPC ex 4 e 5
#Fibonacci no chatgpt "script to give the first 100 terms of fibonacci sequence"


#%%
#EX 4

p = True

q = False

l = p | q

print (l)

#%%
#EX 5

p = True

q = False

w = True

o = p & q;

u = (p | q) & (~q & w)  

print (o)

print(u)

#%%
#EX 6

k = mt.log(16) > 0

print(k)

v = mt.tan(mt.pi/4) > mt.sin(mt.pi/2) 

print(v) 

#%%
#Fibonnaci

a, b = 0, 1
for i in range(100):
    print(a, end=' ')
    a, b = b, a + b

