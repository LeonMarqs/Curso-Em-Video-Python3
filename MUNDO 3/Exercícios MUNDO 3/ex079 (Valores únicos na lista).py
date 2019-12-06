valores = []

while True:
    n = int(input('Digite um valor:  '))
    if n not in valores:
        valores += [n]
    else:
        print('Número já cadastrado')
    continuar = ' '
    while continuar not in 'SN':
        print('--' * 10)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print(f'Você digitou os números : {valores}')
