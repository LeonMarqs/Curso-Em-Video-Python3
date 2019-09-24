print('--'*20)
print('Calculadora de desconto')
print('--'*20)
n = float(input('Digite seu valor: R$'))
p = (n/100)*5
print('Valor com 5% de desconto: R${:.2f}'.format(n-p))
