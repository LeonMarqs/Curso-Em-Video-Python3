from random import randint
from time import sleep
print('-=-'*20)
print ('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
eu = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
pc = randint(0,5)
if eu == pc:
    print('Você ganhou! pensei no número {}.'.format(pc))
else:
    print('Eu ganhei! eu pensei no número {} e não no {}!'.format(pc,eu))
