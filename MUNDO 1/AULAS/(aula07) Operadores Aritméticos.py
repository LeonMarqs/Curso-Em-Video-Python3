# 1° = ()      2° = **       3° = * / // %         4° = - +

n1 = int(input('Um valor: '))
n2= int(input('Outro valor: '))
        #Quebrar a linha
print('A soma de \n {} e {} vale: {}'.format(n1, n2, n1+n2), end=', ')#Para nao quebrar a linha
print('A subtração de {} e {} vale: {}'.format(n1, n2, n1-n2))
print('A multiplicação de {} e {} vale: {:.2f}'.format(n1, n2, n1*n2))
print('A divisão de {} sobre {} vale: {:.2f}'.format(n1, n2, n1/n2))
print('A divisão inteira entre {} e {} é: {}'.format(n1, n2, n1//n2))
print('O resto de {} sobre {} é: {}'.format(n1, n2, n1%n2))
print('A potência de {} elevado a {} vale: {:.2f}'. format(n1, n2, n1**n2))