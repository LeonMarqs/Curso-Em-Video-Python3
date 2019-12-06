# TUPLAS SÃO IMUTÁVEIS

# [-1] = ultimo da tupla

nomes = ('Leo', 'Nessa', 'Genilde', 'José')
idades = (16, 18, 52, 57)

# mostrar apenas valor
''' for c in nomes:
        print(f'{c}', end =' ') '''

# mostrar posicao e valor
'''for cont in range(0, len(nomes)):
    print(f'{nomes[cont]} na posição {cont}')'''

# mostrar a posição e valor
''' for pos, name in enumerate(nomes):
        print(f'{name} na posição {pos}') '''

# Organizar por ordem
'''print(sorted(nomes))'''

#Criar nova tupla a partir de soma de outras
'''c = nomes + idades
print(c)'''

# Contar quantas vezes o valor aparece na tupla
'''print(c.count('Leo'))'''

# Saber a posição do valor
'''print(c.index('Leo'))'''

# Apagar uma variável
'''del(nomes)'''