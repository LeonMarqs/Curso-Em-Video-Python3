from ex107 import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {p:.2f} é {moedas.metade(p):.2f}')
print(f'O dobro de {p:.2f} é {moedas.dobro(p):.2f}')
print(f'Aumentando 10% de {p} é {moedas.aumentar(p, 10)}')
print(f'Diminuindo 13% de {p} é {moedas.diminuir(p, 13)}')
