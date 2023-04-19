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
    
    