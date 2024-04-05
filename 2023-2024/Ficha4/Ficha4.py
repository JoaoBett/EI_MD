# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:07:43 2024

@author: joaog
"""

#%%
#Aula
import math as mt

mt.ceil(100/8)

#%%
#Exercicios
import math as mt

#1
#A
mt.ceil(100/8)

#B
def conversor(x):
    return mt.ceil(x/8)

#2
def inteiro(x):
    if x > 0:
        return mt.floor(x)
    else:
        return mt.ceil(x)
        
inteiro(10.7)
inteiro(-5.3)

#3
def bissexto(x):
    if x % 4 == 0:
        if x % 100 and not x % 400 != 0:
            return print("Nao e bissexto")
    return print("E bissexto")
    
bissexto(2004)


#4
def F(n):
    if n >= 1:
        if n == 1 or n == 2:
            return 1
        if n >= 3 :
            return F(n-1) + F(n-2)
        
F(1000)

#5
def soma_Fib(k):
    soma = 0
    for n in range(1,k+1):
        soma += F(n)
    return soma
    
soma_Fib(5)

#6
import numpy as np

def termos_Fib(s):
    v = np.array([])
    i = 1
    while soma_Fib(i) <=s:
        v = np.append(v, F(i))
        i+= 1
    return v

#7
#A
phi = (1+mt.sqrt(5))/2

n=1
while abs(phi-F(n)/F(n-1))>10**-10:
    n+=1
    
#B

import matplotlib.pyplot as plt
    
Y = np.array([])
for i in range(2,):
    np.append(Y, F(i)/F(i-1))
    
plt.plot(Y)