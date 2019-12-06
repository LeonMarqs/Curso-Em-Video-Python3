from random import randint
from time import sleep
numeros = []

def sortear():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numeros.append(randint(0,10))
        print(f'[{numeros[c]}]', end=' ')
        sleep(0.5)
    print('ACABOU!')


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c

    print(f'A soma deu {soma}')

sortear()
somaPar()