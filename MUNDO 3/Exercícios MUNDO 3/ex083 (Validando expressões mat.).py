n = []

num = str(input('Digite uma expressão: '))

for c in num:
    n+= [c]


parentesesAberto = n.count('(')
parentesesFechado = n.count(')')
if n.index('(') < n.index(')'):
    if parentesesFechado == parentesesAberto:
        print('A expressão é válida!')
else:
    print('A expressão é inválida!')
