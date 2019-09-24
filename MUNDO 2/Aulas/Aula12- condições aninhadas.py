nome = str(input('Qual seu nome? '))
if nome == 'Leonardo':
    print('Que nome lindo!')
elif nome == 'Leandro' or nome == 'Gustavo':
    print('Nome feio')
elif nome in 'Lucas Laur Escanor':
    print('Uau, que legal!')
print('Tenha um bom dia {}!'.format(nome))