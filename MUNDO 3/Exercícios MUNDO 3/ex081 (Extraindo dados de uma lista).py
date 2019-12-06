valores = []

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        print('=='*20)
    if continuar == 'N':
        break
print('=='*20)
print(f'Foram digitados {len(valores)} números')
contrario = valores.sort(reverse=True)
valores.sort(reverse=True)
print(f'A lista de forma decrescente é {valores}')
if 5 in valores:
    print(f'O valor 5 está na lista!')
else:
    print('O valor 5 NÃO está na lista!')
