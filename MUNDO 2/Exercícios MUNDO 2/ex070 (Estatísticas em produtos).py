print('--'*20)
print('         CALCULADORA DE PREÇOS')
print('--'*20)

from time import sleep
barato = ''
cont = 0
mil = 0
qtd = 0
precobarato= 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('=='*20)

    qtd += 1
    if qtd == 1 or preco < precobarato: #nome do mais barato
        barato = nome
        precobarato = preco

    cont += preco
    if preco > 1000:
        mil += 1

    if continuar == 'N':
        break

print(f'o produto mais barato é o(a) {barato} que custa R${precobarato:.2f}')
print(f'O total gasto foi de R${cont:.2f}')
print(f'{mil} produto(s) custam mais de R$1.000,00')
print('{:-^40}'.format(' FIM DO PROGRAMA '))

sleep (10)
