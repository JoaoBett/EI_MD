# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:16:54 2024

@author: joaog
"""

#%%
###################### Aula ######################

#Conjunto vazio
V = set([])


#%%
###################### Exercicios ######################

#%%
A = {1,2,3,4}
B = {3,4,5,6,7}
C = {1,5,9,10}

#A
Universo = A.union(B.union(C))

#B
cardinalidade = len(Universo)

#C
AComp = Universo.difference(A)

#D
DifA = A.difference(B)
 
#E
DifSimetrica = A.symmetric_difference(B)

#%%
#2
a = {0, 1, 2, 4, 8}
b = {3, 5}
c = {4, 6, 8}

#A
Intersecao = a.intersection(c)
res = len(Intersecao)

#B
bc = b.union(c)
resul = a.symmetric_difference(bc)

#%%
#3
def simdiff(A, B):
    union_set = a.union(b)
    
    intersection_set = a.intersection(b)
    return union_set - intersection_set

#%%
#4
z = {0,2,5,8,9}
y = {2,3,5}
uni = {0,1,2,3,4,5,6,7,8,9} 

#A
len(uni.difference(z))

#B
zy = z.symmetric_difference(y)
uzy = uni.intersection(zy)

#%%
#5
Z = set(x for x in range(1, 101) if x % 3 == 0)
Y = set(x for x in range(66, 141) if x % 7 == 0)
W = Z.intersection(Y)

len(Y.intersection(Z.union(W)))

#%%
#6

Catarina = set(range(1, 411))

#A
counter = 0
for x in Catarina:
    if x % 2 == 0 and x % 7 != 0:
        counter += 1
        
#B
quadrados_perfeitos = []

def quadrado_pef(x):
    return int(x ** (1/2)) ** 2 == x

for x in Catarina:
    if quadrado_pef(x):
        quadrados_perfeitos.append(x)

#C
mult3 = []
for x in Catarina:
    if not quadrado_pef(x) and x % 3 == 0:
        mult3.append(x)
        
#%%
#7




#%%
#8
O = {1,2,3,4}
P = {{1},{2},{3,4}}



#%%
#9