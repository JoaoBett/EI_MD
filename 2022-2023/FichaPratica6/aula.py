# -*- coding: utf-8 -*-
"""
Created on Wed May 24 08:24:02 2023

@author: João Bettencourt
"""

#%%

#já falamos no networkx mas nao executamos na aula porque nao havia net e nao 
#estava instalado 
#falamos em matriz de adjacencia
#proixma aula a partir do slide das definiçoes

#importar dados do excel
import pandas as pd

F=pd.read_excel(r"C:\Users\João Bettencourt\Desktop\test.xlsx",header=None) # (r"caminhodoficheiro","folha",header=None)

#(r"caminhodoficheiro","folha",header=None)
#ou se definirem na pasta do canto superior direito
#a pasta onde está o ficheiro
#no lugar do caminho colocar o nome do ficheiro

#aposta a leitura do ficheiro devemos converter em matriz
A=F.to_numpy()

#1b)
import networkx as nx
G=nx.DiGraph(A)
nx.draw_circular(G,with_labels=True)

#%%

def graus(A,k):
    L,C=A.shape
    dout=0
    din=0
    for i in range(0,C):
        dout += A[k-1,i]#fixa linha k-1
        #e percorre as colunas
        din += A[i,k-1]#fixa coluna k-1
        #e percorre as linhas
    return dout, din

sum(A[:,0])
def grauss(A,k):
    return sum(A[k-1,:]),sum(A[:,k-1])

#%%
#ex4

def pocos(A):
    #indique se o grafo tem poços e quais são
    L,C=A.shape
    #percorrer todos os vertices --> linhas/colunas
    #verificar se a soma de cada linha dá zero
    poco=[]
    for i in range(0,L):
        if sum(A[i,:])==0:
            poco.append(i+1)#estamos a adicionar
            #o vertice i+1 pq o i é o indice que inicia em 0 e
            #os vertices inciam em 1
    if poco==[]:
        print("Não temos poços")
    else:
        print("O grafo tem os seguintes poços " + poco)
    
