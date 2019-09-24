import math  # ou from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co,ca) #ou hip = (co **2 + ca ** 2) **(1/2)
print('O valor da hipotenusa é de {:.2f}'.format(hip))

