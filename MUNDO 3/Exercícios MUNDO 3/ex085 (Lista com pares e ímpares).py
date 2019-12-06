lista= [[],[]]

for c in range (1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('=='*20)
print('Lista de pares foram: ',end='')
lista[0].sort()
print(f'{lista[0]}')
print('Lista de ímpares foram: ',end='')
lista[1].sort()
print(f'{lista[1]}')

