print('\033[31m-=-\033[m'*20)
salario = float(input('\033[34mDigite seu salário atual:\033[m R$'))
print('\033[31m-=-\033[m'*20)
if salario < 1250:
    aumento = (salario/100) * 15
else:
    aumento = (salario/100) * 10
atual = aumento + salario
print('O salário que era \033[31;4mR${:.2f}\033[m, agora é \033[32;4mR${:.2f}'.format(salario, atual))
