from random import randint

print('-=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-=-'*15)

vitorias = 0

while True:
    pc = randint(0, 10)
    player = int(input('Digite um número: '))
    jogo = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    print('---'* 15)
    soma = player + pc

    while jogo not in 'PI':
        jogo = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]

    print(f'O computador escolheu {pc} e você {player} = {soma}')
    print('DEU PAR' if soma % 2  == 0 else 'DEU ÍMPAR')
    if soma % 2 == 0 and jogo == 'P':
        print('---'*15)
        print('\033[32mVOCÊ VENCEU!\033[m')
        print('---'*15)
        vitorias += 1

    if soma % 2 == 0 and jogo == 'I':
        print('---' * 15)
        print('\033[31mVOCÊ PERDEU!\033[m')
        break

    elif soma % 2 != 0 and jogo == 'P':
        print('---' * 15)
        print('\033[31mVOCÊ PERDEU!\033[m')
        break

    elif soma % 2 != 0 and jogo == 'I':
        print('---'*15)
        print('\033[32mVOCÊ VENCEU!\033[m')
        print('---'*15)
        vitorias += 1
    print('Vamos novamente...')
    print('==='*15)

print(f'{vitorias} Vitória(s)')
