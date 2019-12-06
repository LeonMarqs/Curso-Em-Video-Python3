from time import sleep

c = ['\033[m',        # 0 - SEM COR
     '\033[0;30;41m', # 1 - VERMELHO
     '\033[0;30;44m', # 2 - AZUL
     '\033[7;30m',    # 3 - BRANCO
     '\033[0;30;43m'  # 4 - AMARELO
]


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    sleep(1.5)
    print(c[3], end ='')
    help(com)
    print(c[0], end='')


def titulo(title, cor=0):
    tam = len(title) + 4
    print(c[cor], end='')
    print('~'* tam)
    print(title.center(tam))
    print('~'* tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca => '))
    if comando.upper() == 'FIM':
        titulo('FIM', 1)
        break
    else:
        ajuda(comando)