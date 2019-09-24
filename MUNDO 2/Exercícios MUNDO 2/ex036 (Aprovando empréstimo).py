casa = float(input('Digite o \033[33;4mvalor da casa\033[m: R$'))
salario = float(input('Digite o seu \033[33;4msalário\033[m: R$'))
anos = int(input('Em quantos \033[33;4manos\033[m pretende pagar? '))

mensal = (casa/anos) / 12
porcento = salario/100 * 30

print('Você pagará \033[4;33m{:.2f}R$\033[m por mês'.format(mensal), end='')
print(' por uma casa de \033[33;4mR${:.2f}\033[m'.format(casa))

if mensal > porcento:
    print('\033[4;31mEMPRÉSTIMO NEGADO\033[m')
else:
    print('\033[32;4mEMPRÉSTIMO ACEITO\033[m\nTenha uma boa compra')
