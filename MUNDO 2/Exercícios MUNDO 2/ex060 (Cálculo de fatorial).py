numero = int(input("Fatorial de: ") )

count= numero
f = 1

while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count >  1 else ' = ', end='')
    f *= count
    count -= 1
print('{}'.format(f))



###################COM MODULO###########################

'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(n)
print('O fatorial de {} é {}'.format(n, fatorial))'''


#################COM FOR######################

'''a = int(input('calcular fatorial de: '))
print('calculando {}! = '.format(a), a, end=' x ')
for c in range(a-1, 0, -1):
    a = a * c
    print(c, end=' x ' if c > 1 else ' = ')
print(a)'''