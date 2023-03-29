# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:02:23 2023

@author: João Bettencourt
"""

L = list()#lista vazia
w='Matemática'
L2=list(w)
#w[3]='E' erro
L2[3]='E'
novastring=''.join(L2)
L1=[-1,3/4,(1,2),[1,2,3],{1},'ab']

#adicionar elementos
L1.append(-1)
L1.insert(3, -1)

L=L1+L2

#remover elementos
L1.pop()#elimina o ultimo elemento da lista
L1.pop(4)


#encontrar elementos
L.index(-1)#sai o 1º indice onde encontra -1
L.count(-1)

#%%
#EX8

P=[{1},{2},{3,4}]
B=[1,2,3,4]
#uniao de tudo é B
U=P[0]|P[1]|P[2]
#insertecao 2 a 2 vazia
I=(P[0]&P[1])|P[0]&P[2]|P[1]&P[2]



#EX9
P=[{1,5},{3},{10,-2},{7,8}],
I=set()
U=set()
for i in range(len(P)):
    U|=P[i]
    for j in range(i+1,len(P)):
        #inicio em i+1 para ser mais eficiente
        #e intersetar apenas conjuntos
        #em posicoes diferentes
        I|=P[i]&P[j]

if I == set():
    print(f'P é partição de {U}')
else:
    print('Não é partição')