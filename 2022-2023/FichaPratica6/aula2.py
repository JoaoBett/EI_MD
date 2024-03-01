# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:34:27 2023

@author: João Bettencourt
"""

#%%
import pandas as pd
import numpy as np

F=pd.read_excel('A_ex2.xlsx', header=None)
A=F.shape

def Br(A,r):
    L,C=A.shape
    B=np.zeros((L,C))
    for i in range(1,r+1):
        B+=np.linalg.matrix_power(A,i)
    return B
#ou
def Br2(A,r):
    L,C=A.shape
    B=A.copy()
    for i in range(2,r+1):
        B+=np.linalg.matrix_power(A,i)
    return B

print(Br(A,8))

#matriz cujas entradas representa o nº de caminhos de comprimento <=8 
#de cada vi e vj

#3)i)

P=Br(A,8)
P[P!=0]=1

#%%

def path(A):
    L,C=A.shape
    Aux=Br(A,L)
    Aux[Aux!=0]=1
    P=Aux
    return P

#TPC
#Alinea 2)b)

#%%

def Warshall(A):
    L,C=A.shape
    P=A.copy()#ponto de partida
    #k vai representar iteraçoes
    for k in range(0,L):
        #cada iteraçao
        #percorrer todas as entradas
        #da matriz
        for i in range(0,L):
            for j in range(0,C):
                if P[i,j]!=1:
                    P[i,j]=P[i,k]&P[k,j]
                    #ou
                    #P[i,j]=P[i,k] and P[k,j]
