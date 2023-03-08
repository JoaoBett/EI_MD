# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 08:15:06 2023

@author: João Bettencourt
"""

#%%
#Teoria
#Biblioteca para arrays
import numpy as np

#Declaracao do array
j = np.array(3)

y = np.array([1,2,3,4,5,6])

m = np.array([[1,2,3],[4,5,6,7,8]])


v = np.array([1,2,3,4])

print(v[0])

v[2] = -100


w = np.arange(-2,10) #np.arange(inicio,limite,step)

u = np.arange(-2,5,0.2)

z = np.linspace(-2,5,49) #np.linspace(inicio,limite,quantidade de elementos)


#introduzir novas entradas no vetor

w = np.append(w, -28)


#Adicionar ao vetor 'z' o vetor 'u'
zu = np.append(z, u)



#Definicao de funcoes

# def namefunction(var1,var2) 

def ola(var):
    print('Ola!',var)

ola('Raul')

def f(x,y):
    out = (x*(y**3)-4*x-2*y)
    return out
    
a = f(1,2)

def ff(x,y):
    return x*y,x/y

b,c = ff(3,4)
d = ff(3,4)

#representação grafica 2D

import matplotlib.pyplot as plt

e = np.linspace(-3,4,50)
g = np.linspace(1, 10,50)

#Representacao de pontos ((x[0],y[0]), (x[1],y[1]))

plt.plot(e,g)
plt.show()

plt.plot(e, g, 'm*')
plt.show()

#colocar nomes debaixo e ao lado do grafico

plt.xlabel('x')

plt.ylabel('y')

#instrucao condicional
#if (condicao):
    #instrucoes
    #else:
        #instrucoes

#Ciclo for
for C in 'palavra':
    print(C)
    
for D in range(-1,5):
    print(D)
    
soma = 0

for E in range(1,45):
    soma+= E
    print(soma)

for G in 'palavra':
    if G == 'v':
        break;
    print(G)
    
#ciclo while
while  