palavras = ('Arroz', 'Feijao', 'Batata', 'Chocolate', 'Fogao', 'Bolo', 'Coxinha')

for c in palavras:
    print(f'\nNa palavra {c} temos: ', end='')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end='')