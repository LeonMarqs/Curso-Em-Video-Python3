pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1] #igual ao peso
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar  not in 'SN':
        continuar = str(input('Quer continuar: [S/N]: ')).strip().upper()[0]
        print('=='*20)
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}kg. Pesos de:',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]',end=' ')
print()
print(f'O menor peso foi de {menor}kg. Pesos de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

