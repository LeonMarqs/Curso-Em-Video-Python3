lista = []
menores = 0
nomeMaisVelho = ''
idadeVelho = 0

for c in range (1, 5):
    print('---- {} PESSOA ----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: ')).strip()
    lista+=[idade]

    if sexo in 'Ff':
        if idade < 20:
          menores += 1 
    if c == 1 and sexo in 'Mn':
        idadeVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Mn' and idade > idadeVelho:
        idadeVelho = idade
        nomeMaisVelho = nome


maior = max(lista)
soma = sum(lista)
media = soma / len(lista)

print('Ao todo são {} menina(s) menores de 20 anos'.format(menores))
print('A média das idades é de {} anos'.format(media))
print('A pessoa mais velha tem {} anos'.format(maior))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeVelho, nomeMaisVelho))

