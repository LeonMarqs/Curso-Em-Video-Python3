lista = []
par = []
impar = []


while True:
    n = int(input('Digite um número: '))
    lista += [n]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        print('=='*20)
        for c in lista:
            if c % 2 == 0:
                par += [c]
            else:
                impar += [c]
        break
print(f'Você digitou os números {lista}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
