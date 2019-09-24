print('--'*20)
print('Conversor de Reais para Dolar')
print('--'*20)
d = float(input('Digite o quanto tem na carteira:R$'))

print('Com R${:.2f}, você pode comprar US${:.2f}'.format(d,d/3.27))