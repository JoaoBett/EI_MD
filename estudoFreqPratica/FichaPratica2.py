import numpy as np
import matplotlib.pyplot as plt

#1
#a
def f(x):
    resultado = np.cos(x) + np.e**x
    return resultado

#b
a = f(0)
print(a)

b = f(np.pi)
print(b)

input("")

#c
X = np.linspace(1,2,98)

#d
j = f(X)
print(j)

#2
def g(x):
    resultado = (x**5) - (3*x**4) - (3*x**3) + (7*x**2) + (6*x)
    return resultado

x = np.arange((-1,5),(2,5),0,125)
z = g(x)
plt.plot(x,z)
plt.show()
