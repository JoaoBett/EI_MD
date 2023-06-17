import math as mt
#3
#a
a = 15.62
b = -7.08
c = 62.5
d = 0.5*(a*b-c)

result = a + (((a*b)/c)*(((a+d)**2)/(mt.sqrt(abs(a*b)))))
#b
print(result)
input("")

#4
p = True
q = False
isTrue = p or q

print(isTrue)
input("")

#5
#a

w = True
valor_logico = p and q
print(valor_logico)

#b
valor_logico2 = (p or q) and (not q and w)
print(valor_logico2)

