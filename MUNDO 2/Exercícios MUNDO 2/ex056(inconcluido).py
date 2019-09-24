somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4

print('Ao todo são {} menina(s) menores de 20 anos'.format(totmulher20))
print('A média das idades é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))