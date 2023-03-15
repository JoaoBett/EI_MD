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
    out = (np.cos(x) + (np.e**x))
    return out

#b)
a = f(0)

b = f(np.pi)

#c)
X = np.linspace(1, 2,98)


#d)

print(f(X))    

#e)

y = f(X)
plt.plot(X,y)
plt.show()

#%%
#EX 2

def g(x):
    out = ((x**5)-(3*x**4)-(3*x**3)+(7*x**2)+(6*x))
    return out

x = np.arange(-1.5, 2.5,0.125)
z = g(x)
plt.plot(x,z)
plt.show()

#%%
#EX 3
def r(x):
    out = (10*((0.5)**(x/140)))
    return out

t = 0
for x in range(0,10):
    t +=7
    print(r(t))

x = np.arange(0,10,7)
y = r(x)

plt.plot(x,y)
plt.show()
#%%
#EX 4
#a)
def z(k):
    return(1/2)**k


for x in range(1,21):
    print(z(x))
    
t=np.arange(1,21,1)
c=z(t)
plt.plot(t,c)
plt.xlabel('c(quantidade)')
plt.ylabel('t(tempo)')
plt.title('Gráfico da função z(n)')
plt.show()

#b
def z(k):
    return(1/2)**k


x=1

while r > (10**-10):
    r=abs((z(x)-z(x-1)))
    print(r)
    if r < (10**-10):
        print(r)
        break
    x+=1


#%%
#EX 5

#a)
termos = []
for n in range(1, 71):
    if n % 3 == 0:
        termos.append(2**-(n/10)*(n/3))
    else:
        termos.append(3**-(n/10)*n)

# plotar um gráfico dos termos
plt.plot(termos)
plt.xlabel('Índice n')
plt.ylabel('Termo Sn')
plt.title('Gráfico dos primeiros 70 termos da sucessão S')
plt.show()


#b)
#Função soma que soma todos os n primeiros termos da função Sn
def soma(n):
    resultado = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            resultado += (2**(-(i/10))*(i/3))
        else:
            resultado += (3**(-(i/10))*i)
    return resultado


#Função primeiro numero, que só retorna o primeiro numero de n onde a soma é 42
def primeiro_n():
    n = 0
    while soma(n) <= 42:
        n += 1
    return n


#Aplicar a função
print(primeiro_n())





