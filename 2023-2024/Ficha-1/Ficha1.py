# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:34:38 2024

@author: joaog
"""

import math

#1
#A
x = (35.6*64-7**3)/(45+5**2)
print(x)

#B
y=(5/7)*4*(6**2)-((3**7)/(9**3)-236)
print(y)

#C
z = ((3**2) * math.log10(76) / (7**3) + 54) + (910 ** (1/3))
print(z)

#D
w = (math.cos((5*math.pi)/6)**2)*(math.sin((7*math.pi)/8)**2) + (math.tan((math.pi/6)*math.log(8, math.e))/math.sqrt(7))
print(w)

#2
#A
X = 13.5
a = (X**3)-(2*X)+(23.5*(X**2))
print(a)

#B
b = math.sqrt(14*(X**3))/math.e**(3*X)
print(b)

#C
c = math.log(abs((x**2)-(x**3)))
print(c)


#3
#A
A=15.62
B=-7.08
C=62.5
D=0.5*((A*B)-C)

resultado = A + (((A*B)/C)*((A+D)**2)/math.sqrt(abs(A*B)))
#B
print(resultado)

#4
p = True
q = False

boleanos = p or q
print(boleanos)

#5
#A
P = True
Q = False
W = True

boleanos2 = P and Q
print(boleanos2)

#B
boleanos3 = (P or Q) and (not Q and W)
print(boleanos3)

#6
#A
expressoes = math.log(16) > 0
print(expressoes)

#B
tangente = math.tan(45) > math.sin(90)
print(tangente)