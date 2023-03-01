# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:49:11 2023

@author: João Bettencourt
"""
#Comentários
#import de bibliotecas 
#'as' é para mudar o nome da biblioteca
import math as mt

#dar um scan e um print para o utilizador
d = input('Introduza a quantidade de dolares:')

#input vem sempre em string(str)

#Transformar o input em int
d = int(d)

#multiplicação
d *= 2

#Prints
print(d)

#seno
mt.sin(d/6)

#logaritmo
mt.log10(2)

#logaritmo de base n = ln
mt.log(5)