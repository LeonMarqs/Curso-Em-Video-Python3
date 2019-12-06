produtos = ('Guitarra', 700, 'Baixo', 900, 'Capotraste', 5, 'Palheta', 2, 'Amplificador', 500, 'Cabos', 100 , 'Interface', 1000)

print('=='*20)
print('{:^40}'.format('TABELA DE PREÇOS'))
print('=='*20)

for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')




