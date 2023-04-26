# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 08:20:13 2023

@author: João Bettencourt
"""

#%%

#Funcoes inteiras
#floot
import math as mt

mt.floor(5.2)

mt.floor(-2.3)

#de entre todos os inteiros menores ou iguais a 5.2 escolhe o maior

#Celling

mt.ceil(5.2) #6

mt.ceil(-1.3) #-1

#de entre todos os inteiros maiores ou iguais a x mt.ceil(x) escolhe o menor
#%%
#inteiro

int('3')=3

int(5.2)=5

int(5.9)=5

#%%
#ex10_ficha4

serie='M500 27 55 87 01'

n=input('Insira o nº de serie: ')

beta=Letras.index(n[o])+1

Letras='RSTUMN'
Letras=list(Letras)

soma=Letras.index(n[0])+1

#sai o indice +1 onde se encontra a primeira letra do numero de serie

for x in n[1:len(n)]:
    soma +=int(x) #transforma cada caractere numero em inteiro para somar
    
if soma%9 == 0:
    print('válido')
else:
    print('invalido')

#%%
#Ficha5

#Relacoes
import numpy as np

#M = ([a1,a2,...],[b1,b2,...])

#multiplicar matrizes
#A@B

#Potenciação de matrizes (A**3=[aij**3])

#A^3 = A@A@A

#np.linalg.matrix_power(A, 3)
 
#Aceder a elementos da matriz

#M[i,j]

#M[1,2] --> aceder ao elementos que esta na linha 2 e na coluna 3

#M[:,3] --> toda a quarta coluna

#M[2,:] 

#M[:,1:4] --> parte da 3 linha compreendida entre a segunda coluna e a 4 coluna(exclusive) 




#Matrizes Especiais

I4=np.eye(4)

O=np.ones((L,C))
Z=np.zeros((L,C))
 

#Dimensões da matriz

O.shape

#Transposta da Matriz

O.T

#%%
#Ficha 5 - Exs

#1
#a)
MR=np.array([[1,0,1,0],[1,0,1,0],[1,1,0,0]])

#b)

MR_inv=MR.T

#c)é uma especie do produto MR^2
#RoR

MR2=MR@MR

def um(M):
    #percorrer a matriz e se encontrar algum elemento maior que 1 torna-lo num 1
    
    L,C=M.shape
    for i in range(0,L):
        for j in range(0,C):
            if M[i,j]>1:
                M[i,j]=1
    return M

MR2=um(MR2)

MR3=MR@MR@MR #ou
MR3=np.linalg,matrix_power(MR,3)
MR3=um(MR3)  #ou
MR3[MR3>1]=1


#%%
#ex 4
#a)

def is_reflexiva(M):
    for i in range(len(M)):
        
        if M[i][i] != 1:
            return False
        
        for j in range(len(M)):
            if i!=j and M[i][j]!=0:
                return False
        
    return True;

#2 maneira de fazer
def is_reflex(M):
    L,C=M.Shape
    logico=True
    
    for i in range(0,L):
        if M[i,i]==0:
            return False
    
    return logico

#3 maneira de fazer
def is_reflexiv(M):
    L,C=M.shape
    return np.trace(M)==L

#4 maneira de fazer
def is_refle(M):
    L,C=M.shape
    return (np.diag(M)==np.diag(np.eye(L))).all()

#b)
def is_simetrica(M):
    L,C=shape(M)
    for i in range(0,L):
        for j in range(i+1,C):
            if M[i,j]!=M[j,i]:
                return False
    return True


def is_simet(M):
    return (M==M.T).all()