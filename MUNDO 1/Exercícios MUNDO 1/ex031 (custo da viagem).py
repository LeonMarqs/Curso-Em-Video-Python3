print('-=-'* 20)
viagem = float (input('Quantos km será a viagem? '))
print('-=-'*20)
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('Você fará uma viagem de {}km, o custo será de R${:.2f}'.format(viagem, preco))