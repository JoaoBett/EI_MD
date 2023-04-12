# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:20:32 2023

@author: João Bettencourt
"""
#%%
def u(n):
    if n==1:
        return 2
    elif n==2:
        return 6
    elif n>=3:
        return 2*u(n-1)+4*u(n-2)
    else:
        print('Insira um valor válido')
    
def u(n):
    if n==1:
        return 2
    elif n==2:
        return 6
    elif n>=3:
        un_1 = 6
        un_2 = 1
        for i in range(3,n+1):
            un=2*un_1+4*un_2
            un_2=un_1
            un_1=un
        return un
    else:
        print('Insira um valor válido')

#%%
#Teste prático 21/22

#(C) Vn=un+1/un

#V1=u2/u1

#V2=u3/u2

import matplotlib.pyplot as plt

#plt.plot(x,y,'*')

import numpy as np

x=np.arange(1,21)
y=np.array([])

for i in x:
    y=np.append(y,u(i+1)/u(i))
plt.plot(x,y,'*')
plt.show()


#%%

X=list(range(1,21))
Y=list()
for i in X:
    Y.append(u(i+1)/u(i))
    
    
    
#%%
#FichaPratica4
#4

def f(n):
    if n==1 & n==2:
        return 1
    elif n>=3:
        fn_1=1
        fn_2=1
        for i in range(3,n+1):
            fn=fn_1+fn_2
            fn_2=fn_1
            fn_1=fn
        return fn
    else:
        print('Erro - Insira um valor válido')
        
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
#print(f(10))
#print(f(40))
        
#%%
#5

def soma_fib(k):
    a = 1
    b = 1
    for i in range(k):
        print(a)
        soma =+ a
        a, b = b, a + b
    return soma

def G(n):
    Y=[1,1]
    for i in range(3,n+1):
        Aux=Y[i-1]+Y[i-2]
        Y.append(Aux)
    return Y
        
#%%
#6

def termos_fib(s):
    v=list()
    k = 1
    while soma_fib(k)<=s:
        v.append(G(k))
        k=+1
    return v

#%%

#TPC EX3