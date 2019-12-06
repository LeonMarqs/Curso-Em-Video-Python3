from ex109 import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10% é {moedas.aumentar(p, 10, True)}')
print(f'Diminuindo 13% é {moedas.diminuir(p, 13, True)}')