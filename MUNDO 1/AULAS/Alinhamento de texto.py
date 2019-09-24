nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer {:20}!'.format(nome))

# Alinhado a direita
print('Prazer em te conhecer {:>20}!'.format(nome))

# Alinhado a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))

# Centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))

# Com simbolos em volta
print('Prazer em te conhecer {:=^20}!'.format(nome))