import random
print('-=-'*10)
print('JOKENPÔ GAME')
print('-=-'*10)
voce = str(input('Escolha sua jogada: ')).capitalize()
jokenpo = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(jokenpo)

if voce == 'Pedra' and  pc == 'Pedra':
    print('EMPATE, o PC escolheu {}'.format(pc))

elif voce == 'Pedra' and  pc == 'Papel':
    print('VOCÊ PERDEU, o PC escolheu {}'.format(pc))

elif voce == 'Pedra' and  pc == 'Tesoura':
    print('VOCÊ GANHOU, o PC escolheu {}'.format(pc))

elif voce == 'Papel' and  pc == 'Pedra':
    print('VOCÊ GANHOU, o PC escolheu {}'.format(pc))

elif voce == 'Papel' and  pc == 'Tesoura':
    print('VOCÊ PERDEU, o PC escolheu {}'.format(pc))

elif voce == 'Papel' and  pc == 'Papel':
    print('EMPATE, o PC escolheu {}'.format(pc))

elif voce == 'Tesoura' and  pc == 'Pedra':
    print('VOCÊ PERDEU, o PC escolheu {}'.format(pc))

elif voce == 'Tesoura' and  pc == 'Papel':
    print('VOCÊ GANHOU, o PC escolheu {}'.format(pc))

elif voce == 'Tesoura' and  pc == 'Tesoura':
    print('EMPATE, o PC escolheu {}'.format(pc))


