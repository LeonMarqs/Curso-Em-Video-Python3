jogador = {}
totgols = []
galera = []
while True:
    jogador.clear()
    nome = str((input('Nome do jogador: ')))
    jogador['nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    totgols.clear()

    print('=='*20)

    for c in range (0, partidas):
        gols = int(input(f'Quantos gols {nome} fez na partida {c+1}? '))

        totgols += [gols]

    jogador['gols'] = totgols[:]
    jogador['total'] = sum(totgols)
    galera.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas com [S] ou [N].')
    if continuar == 'N':
        break

print('=='*20)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('=='*20)

for k, v in enumerate(galera):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=='*20)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(galera):
        print('ERRO! Não existe jogador com tal código')
    else:
        print(f'LEVANTAMENTO DE DADOS DO JOGADOR {galera[busca]["nome"]}')
        for index, gols in enumerate(galera[busca]["gols"]):
            print(f' => No jogo {index+1} fez {gols} gols')
    print('-'*30)
print('<<< VOLTE SEMPRE >>>')
