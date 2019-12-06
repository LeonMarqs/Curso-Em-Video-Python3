extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')




while True:
    numero = int(input('Digite um número: '))

    while numero not in range(0,21):
            numero = int(input('Digite novamente: '))

    print(f'Você digitou o número {extenso[numero]}')
    continuar = ' '
    while continuar not in  'SN':
        continuar = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
        print('=='*20)

    if continuar == 'N':
        print('Fim do programa')
        break