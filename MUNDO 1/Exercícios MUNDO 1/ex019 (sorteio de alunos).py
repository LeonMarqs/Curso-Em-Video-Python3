import random
one = str(input('Primeiro aluno: '))
two = str(input('Segundo aluno: '))
tree = str(input('Terceiro aluno: '))
four = str(input('Quarto aluno: '))
lista =  [one, two, tree, four]
sorteio = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteio))