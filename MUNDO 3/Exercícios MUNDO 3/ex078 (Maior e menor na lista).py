lista = []

for c in range (0, 6):
    n = int(input(f'Digite um número para a posição {c}: '))
    lista += [n]

print('=='*20)
print(f'Você digitou os valores: {lista}')
enumerate (lista)
#maiorIndex = lista.index(max(lista))
#menorIndex = lista.index(min(lista))
maior = max(lista)
menor = min(lista)
print(f'Maior valor = {maior} na posição', end=' ')
for v, c in enumerate(lista):
    if c == maior:
        print(f'{v}...', end=' ')
print(f'\nMenor valor = {menor} na posição', end=' ')
print(lista)
for v, c in enumerate(lista):
    if c == menor:
        print(f'{v}...', end=' ')

#if lista.count(maior) > 1:
   # print(maiorIndex)