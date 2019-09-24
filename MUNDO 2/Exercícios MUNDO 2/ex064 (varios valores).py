n = 1
lista = []

while n != 999:
    n = int(input('Digite um valor [999 para parar]:  '))
    if n != 999:
        lista += [n]

soma = sum(lista)
numeros = len(lista)

print('Você digitou {} números'.format(numeros))
print('A soma entre eles é de {}'.format(soma))
