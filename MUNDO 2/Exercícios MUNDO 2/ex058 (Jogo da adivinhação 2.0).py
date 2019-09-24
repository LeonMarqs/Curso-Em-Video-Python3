from random import randint
from time import sleep
print('-=-'*20)
print ('Vou pensar em um \033[35mnúmero entre 0 e 10\033[m, tente adivinhar...')
print('-=-'*20)

lista = []
pc = randint(0, 10)
player = int(input('Em que número eu pensei? R: '))
print('PROCESSANDO...')
sleep(1)
while player != pc:
    if player > pc:
        player = int(input('Menos! Tente novamente! R:'))
        lista += [player]
    else:
        player = int(input('Mais! Tente novamente! R:'))
        lista += [player]
tentativas = len(lista) + 1

print('Parabéns, você acertou!')
print('Precisou de {} tentativas'.format(tentativas))
