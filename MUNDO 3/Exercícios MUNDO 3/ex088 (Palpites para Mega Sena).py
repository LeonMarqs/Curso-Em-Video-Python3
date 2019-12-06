from random import randint
from time import sleep
dados = []
megasena = []
print('=='*20)
print('{:^40}'.format('MEGA-SENA'))
print('=='*20)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-= SORTEANDO {n} JOGOS -=-=-=-=-')

for c in range (1, n+1):
    for d in range(0, 6):
        n2 = (randint(0, 60))
        if n2 not in dados:
            dados.append(n2)
        else:
            n2 = (randint(0, 60))
            dados.append(n2)
    megasena.append(dados)
    print(f'Jogo {c}: {dados}')
    dados.clear()
    sleep(1)
print('=='*20)