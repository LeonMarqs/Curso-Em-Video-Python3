from datetime import date
atual = date.today().year

contmaior = 0
contmenor = 0


for c in range (1, 8):
    nasc = int(input('\033[35mDigite o ano de nascimento do\033[m {}: '.format(c)))
    idade = atual - nasc
    if idade < 0:
        print('\033[31mEssa pessoa não nasceu ainda\033[m')
    elif idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
print('São \033[32m{} pessoas maiores de idade\033[m\nE \033[34m{} pessoas menores de idade\033[m'.format(contmaior, contmenor))


