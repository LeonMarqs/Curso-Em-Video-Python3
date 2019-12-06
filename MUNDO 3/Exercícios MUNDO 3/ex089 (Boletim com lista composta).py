boletim = []
while True:
    aluno = [[], []]
    aluno[0].append(str(input('Nome: ')))
    aluno[1].append(float(input('Nota 1: ')))
    aluno[1].append(float(input('Nota 2: ')))
    boletim.append(aluno[:])
    aluno.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]: ')).strip().upper()[0]
        print('=='*20)
    if continuar == 'N':
        break
print('=='*20)
print('No.   NOME          MÉDIA')
print('--'*15)
# [ [['NOME'], [NOTAS, NOTAS], [['NOMES],[NOTAS, NOTAS]] ]
pos = 0
for c, v in enumerate(boletim):  #posicao, valor
    media = sum(boletim[pos][1]) / 2
    print(f'{c}  {v[0][0]}    {media}')
    pos += 1

while True:
    print('=='*20)
    n = int(input('Mostrar notas de qual aluno? [999 encerra]: '))
    print(f'Notas de {boletim[n][0]} são {boletim[n][1]}')
    if n == 999:
        break
