print('\033[30m-=-'*20)
v = float(input('Qual a velocidade atual do carro? '))
print('-=-'*20)
multa = (v - 80) * 7
if v > 80:
    print('\033[30mVocê foi \033[31mmultado\033[m \033[30mpor exceder o limite de \033[32m80km/h\033[30m\n A multa custará R${:.2f}'.format(multa))
    print('-=-'*20)
print('Tenha um bom dia! Dirija com segurança!')
