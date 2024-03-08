# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:04:06 2024

@author: joaog
"""
#%%

import numpy as np
import matplotlib.pyplot as plt

#%%

###################### AULA ######################

primeiro = np.array([1,2,3,4,5])

arrays_grandes = np.arange(1,100,1 )

segundo_array = np.arange(1, 6, 1)

pares = np.arange(2,20,2)

v = np.linspace(5,15,5)

np.append(v, 56)

v = np.append(v, 56)

def somas(x,y,z):
    s = x+y+z
    return s

somas(1,2,3)

def f(x):
    return x**2

f(5)
###################### EXERCICIOS ######################
#%%
#1
#A
def f(x):
    return np.cos(x) + np.e**x

#B
zero = f(0)
pi = f(np.pi)
    
#C
X = np.linspace(1, 2, 98)

#D
print(f(X))
#%%

#2
def g(x):
    return (x**5) - (3*(x**4)) - (3*(x**3)) + (7*(x**2)) + (6*x)

x = np.arange(-1.5, 2.5, 0.125)
z = g(x)
plt.plot(x, z)
plt.show()

#%%

#3
def r(x):
    return 10*(0.5)**(x/140)

t = 0
for t in range(0,10):
    t += 7
    print(r(t))

graf = r(x)

a = np.arange(0,10,7)
b = r(x)

plt.plot(a,b)
plt.show
#%%

#4
#A
def z(k):
    return (1/2)**k

for c in range(1,21):
    print(z(c))
    
D=np.arange(1,21,1)
d=z(D)
plt.plot(D,d)
plt.xlabel('c(quantidade)')
plt.ylabel('t(tempo)')
plt.title('Gráfico da função z(n)')
plt.show

#B
x=1

while r > (10**-10):
    r=abs((z(x)-z(x-1)))
    print(r)
    if r < (10**-10):
        print(r)
        break
    x+=1
#%%
    
#5
#A
def soma(x):
    resultado = 0
    for i in range(1,x+1):
        if x % 3 == 0:
            resultado = (2**-(x/10)) * (x/3)
        else:
            resultado = (3**-(x/10)) * x
    return resultado

E=np.arange(1,71,1)
e=z(D)
plt.plot(E,e)
plt.show

#B
def primeiro_num():
    n=0
    while soma <= 42:
        n+=1    
    return n

print(primeiro_num())