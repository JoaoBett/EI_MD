# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:12:51 2023

@author: João Bettencourt
"""

#%%
#Ex12
#b)
#------->5 0 2 7 8 1 1 0 2 0 1 0 3 X

#Multiplicar
#------->2x

#------->10 0 4 16 1 1 2 0 4 0 2 0 6 X
#------->1 0 4 7 7 1 2 0 4 0 2 0 6 X = 34+X

#------->X = 6

#b)
nc='40212888881882'
def autenticar_cartao(nc):
    L=list(nc)
    L.reverse()
    #reverter o numero
    #somente percorrer lista para transformar tudo em inteiro
    for i in range(0,len(L)):
        L[i]=int(L[i])
    #Assim basta começar na posição 1 e ir ate ao fim
    for i in range(1,len(L),2):
     L[i]=L[i]*2
     if L[i]>9:
         L[i]=L[i]//10+L[i]%10
     if sum(L)%10==0:
         print('Cartao válido')
     else:
         print('Cartao inválido')

def autenticar_cartao2(nc):
    L=list(nc)
    for i in range(0,len(L)):
        L[i]=int(L[i])
    #começar na penultima posicao
    for i in range(len(L)-2,0,-2):
     L[i]=int(L[i])*2
     if L[i]>9:
         L[i]=L[i]//10+L[i]%10
     if sum(L)%10==0:
         print('Cartao válido')
     else:
         print('Cartao inválido')
