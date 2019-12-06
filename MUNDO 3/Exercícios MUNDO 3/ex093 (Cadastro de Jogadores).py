jogador = {}
totgols = []

nome = str((input('Nome do jogador: ')))
jogador['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))
print('=='*20)

for c in range (0, partidas):
    gols = int(input(f'Quantos gols {nome} fez na partida {c}? '))
    totgols += [gols]

print('=='*20)

jogador['gols'] = totgols
jogador['total'] = sum(totgols)
print(jogador)

print('=='*20)

for k, v in jogador.items():
    print(f'O campo {k} tem valor de {v}.')

print('=='*20)


print(f'O jogador {nome} jogou {partidas} partidas')
for p, v in enumerate(totgols):
    print(f'=> Na partida {p} fez {v} gols ')
print(f'Foi um total de {sum(totgols)} gols')

