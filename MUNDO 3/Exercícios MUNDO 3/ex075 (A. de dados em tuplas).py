numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

valor9 = numeros.count(9)

#pares = numeros.

print(f'O número 9 foi digitado {valor9} vezes')
if 3 in numeros:
    pos3 = numeros.index(3)
    print(f'O número 3 foi digitado na {pos3 + 1} posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares foram: ', end='')

for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end= ' ')

