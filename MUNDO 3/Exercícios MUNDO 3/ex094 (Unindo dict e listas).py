lista_pessoas = []
pessoa = {}
soma = media_idades = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Tente novamente com M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista_pessoas.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if continuar == 'N':
        break

print('=='*20)

pessoas_cadastradas = len(lista_pessoas)
media_idades = soma / pessoas_cadastradas

print(f'A) Ao todo temos {pessoas_cadastradas} pessoas cadastradas.')
print(f'B) A média das idades cadastradas é de {media_idades:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in lista_pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='... ')
print()

print('D) Lista as pessoas que estão acima da média:')
for p in lista_pessoas:
    if p['idade'] >= media_idades:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')

print('\n  <<< ENCERRADO >>>')
