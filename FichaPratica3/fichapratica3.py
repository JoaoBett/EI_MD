# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 08:16:24 2023

@author: João Bettencourt
"""

#Sets

V = set() # cria um conjunto vazio 

A = {-1,2,3,5,-1,2} #cria um conjunto
                    #Atencao {} Nao cria conjunto vazio = cria um dictionary
                    
B = {-12,3,3/4,'ab',(1,2)}

#Podemos definir conjuntos de varios tipos de elementos
#Mas nao conseguimos defenir cojunto de cojuntos

#Para isto vamos usar o datatype List

#Listas

L1 = [1,'ab',15,[1,2]]

L1[0]

L2 = [{1},{2,3},{4,5}]

L1[3] = [1,2]

L1[3][1]


#Continuando conjuntos
#criar conjuntos de forma automatica

C = set([-1,2,3,2])

D = set('Matemática')

E = set(range(-2,15,2))

F = {}

#{Expressão for var in sequencia}

#{Expressao for var in sequence if condition}

H = {x for x in 'Matemática' if x not in 'discreta'}

#Adicionar elementos

A.add(-25)

#A.add({-10,5,6}) #Erro

#Operacoes com cojuntos

#Uniao

I = A|B 

#ou

I = A.union(B)

#Interseção

J = A&B

#ou

J = A.intersection(B)

#Diferença de A e B

A-B

#ou

A.difference(B)

#Diferença simétrica
#A.uniao(B) - A.interseçao(B)

A^B

#(A|B) - (A&B)

#(A-B) | (B-A)

#Cardinalidade de cojuntos finitos de elementos

len(A)  #nº de elemntos de conjuntos

#remover elemntos

A.remove(2)

A.discard(2)

