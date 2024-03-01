# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:11:56 2023

@author: João Bettencourt
"""

#%%
#5
#c)

import numpy as np

def is_transitiva(F):
    for x,y in F:
        for z,w in F:
            if y == z and (w,x) not in F:
                return False
    return True
    
#ou

def is_transitiv(M):
    M2=np.linalg.matrix_power(M,2) #M@M
    M2[M2!=0]=1 
    L,C=M.shape
    for i in range(0,L):
        for j in range (0,C):
            if M[i,j]==0 and M[i,j]!=M2[i,j]:
                return False
    return True

#ou

def is_transit(M):
    M2=np.linalg.matrix_power(M,2) #M@M
    M2[M2!=0]=1 
    Mm=M+M2
    Mm[Mm!=0]=1
    return (M==M).all()
    

def fecho_transitivio(M):
    if is_transitiva(M):
        return M
    else: #nao e transitiva temos de calcular o fecho
    #transitivo(R)=RUR^2UR^3U...UR^n n=nº de elementos de A
    #MATRIZ2=MATRIZ R + MARTRIZ^2...
    #MATRIZ tudo diferende 0 passa a 1
        L,C=M.shape
        A=M #atenção
        for i in range(2,L+1):
            A+=np.linalg.matrix_power(M,i)
        A[A!=0]=1
        return A
    
def equival(M):
    if is_reflexiva(M) and is_simetrica(M) and is_transitiva(M):
        print('A relacao é uma relacao de equivalencia')
    else:
       return fecho_transitivo(fecho_simetrico(fecho_reflexivo(M)))
    