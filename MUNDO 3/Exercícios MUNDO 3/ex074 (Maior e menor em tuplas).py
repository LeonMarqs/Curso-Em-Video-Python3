from random import randint

sorteados = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Sorteei os valores:', end= ' ')
for c in sorteados:
    print(f'{c}', end=' ')

menor = min(sorteados)
maior = max(sorteados)

print(f'\nO menor valor foi {menor}')
print(f'O maior valor foi {maior}')