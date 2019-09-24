from random import randint
from time import sleep

print('\033[34m-=-'*10)
titulo = 'JOKENPÔ GAME'
print('{:^30}'.format(titulo)) #alinhado no centro
print('-=-'*10)
print('''\033[mSuas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual sua jogada?: '))


while jogador < 0 or jogador > 2:
    jogador = (int(input('Digite novamente!! ')))


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-' * 10)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 10)

if computador == 0: # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU\033[m')


elif computador == 1: #  PAPEL
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU\033[m')


elif computador == 2: # TESOURA
    if jogador == 0:
        print('\033[32mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('EMPATE')


