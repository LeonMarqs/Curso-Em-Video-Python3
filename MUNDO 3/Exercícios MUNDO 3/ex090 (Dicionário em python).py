nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))

aluno = {'Nome':nome, 'Media':media}
print('=='* 15)
if media >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= media < 7:
    aluno['Situação'] = 'Recuperação'
    for k, v in aluno.items():
        print(f'{k} é igual a {v}')
else:
    aluno['Situação'] = 'Reprovado'

    for k, v in aluno.items():
        print(f'{k} é igual a {v}')


