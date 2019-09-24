preco = float(input('Digite o valor do produto: '))
pagamento = int(input('FORMAS DE PAGAMENTO:\n[1] À vista dinheiro/cheque\n[2] À vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\n Qual dessas é a sua opção? '))

dinheiro = ((preco * 10) / 100)
cartao =  ((preco * 5) / 100)
cartao2x = preco
cartao3x = ((preco * 20) / 100)

if pagamento == 1:
    print('Você vai pagar R${:.2f}'.format(preco - dinheiro))
elif pagamento == 2:
    print('Você vai pagar R${:.2f}'.format(preco - cartao))
elif pagamento == 3:
    print('Você vai pagar R${:.2f}'.format(cartao2x))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Você vai pagar R${:.2f}'.format(preco + cartao3x))
else:
    print('Opção INVÁLIDA, tente novamente.')
