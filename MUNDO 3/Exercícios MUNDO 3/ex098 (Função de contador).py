from time import sleep

def linha():
    print('=='*20)


def contagem(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)
    if inicio < fim:
        if passo != 0:
            if passo > 0:
                for c in range(inicio, fim + 1, passo):
                    print(c, end=' ')
                    sleep(0.5)
            elif passo < 0:
                passo *= -1
                for c in range(inicio, fim + 1, passo):
                    print(c, end=' ')
                    sleep(0.5)
        else:
            passo = 1
            for c in range(inicio, fim + 1, passo):
                print(c, end=' ')
                sleep(0.5)

    elif inicio > fim:
        if passo != 0:
            if passo > 0:
                passo *= -1
                for c in range(inicio, fim - 1, passo):
                    print(c, end=' ')
                    sleep(0.5)
            elif passo < 0:
                for c in range(inicio, fim - 1, passo):
                    print(c, end=' ')
                    sleep(0.5)
        else:
            passo = -1
            for c in range(inicio, fim - 1, passo):
                print(c, end=' ')
                sleep(0.5)
    print()
linha()

contagem(1, 10, 1)
linha()
contagem(10, -1, 2)
linha()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)

linha()