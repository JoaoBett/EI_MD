# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 08:13:44 2023

@author: João Bettencourt
"""

#%%
import numpy as np

def Warshall_Min(W):
    Q=W.copy()
    Q=Q.astype(float)
    Q[Q==0]=np.inf
    L,C=W.shape
    M=np.empty((L,C))
    M=M.astype(str)
    for i in range(0,L):
        for j in range(0,C):
            if W[i,j]==0:
                M[i,j]='-'
            else:
                M[i,j]=str(i+1)+str(j+1)
    #indice para as interaçoes
    for k in range(0,L):
        #em cada interaçao percorremos
        #todas as entradas
        for i in range(0,L):
            #se a entrada Q
            #tiver maior custo
            #substituimos pela nova
            #ligacao
            for j in range(0,C):
                #se a entrada Q[i,j]]
                #tiver maior custo substituimos pela nova ligação
                if Q[i,j]>Q[i,k]+Q[k,j]:
                    Q[i,j]=Q[i,k]+Q[k,j]
    return Q,M#cada execucao sai 2 matrizes
#a matriz dos custos minimos Q
#a matriz dos caminhos correspondentes aos custos minimos

#Q,M=Warshall_Min(W)
#print(Q)
#print(M)

import panda as pd

A=pd.read_excel('grafos_f7.xls',header=None)

D=pd.read_excel('grafos_f7.xls','Duração',header=None)
D=D.to_numpy()

C=pd.read_excel('grafos_f7.xls','Custo',header=None)
C=C.to_numpy()

I=pd.read_excel('grafos_f7.xls','Identificações',header=None)
I=I.to_numpy()

#ex4b
i=2
j=5
def viagem_custo(C,D,I,i,j):#viagem_custo(Matriz custo, matriz duracao, 
#matriz identificaçoes, partida, chegada)
#(C,D,I,2,5)
    
    