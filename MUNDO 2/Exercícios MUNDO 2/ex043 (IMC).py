peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura*altura)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[34;4mAbaixo do peso\033[m')
elif imc <= 25:
    print('\033[32;4mPeso ideal\033[m')
elif imc <= 30:
    print('\033[33;4mSobrepeso\033[m')
elif  imc <= 40:
    print('\033[31;4mObesidade\033[m')
elif imc > 40:
    print('\033[35;4mObesidade Mórbida\033[m')
