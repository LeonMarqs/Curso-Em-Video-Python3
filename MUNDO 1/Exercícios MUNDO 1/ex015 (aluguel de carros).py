d = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km rodados? '))
f = (d * 60) + (0.15 * km)
print('O valor total a se pagar  é de: R${:.2F}'.format(f))