numero = int(input('Digite um número para conversão: '))
print('''Escolha uma das opções abaixo
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL ''')
base = int(input('Sua opção: '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

if base == 1:
    print('{} convertido para BINÁRIO é \033[33;4m{}\033[m'.format(numero, binario))
elif base == 2:
    print('{} convertido para OCTAL é \033[33;4m{}\033[m'.format(numero, octal))
elif base == 3:
    print('{} convertido para HEXADECIMAL é \033[33;4m{}\033[m'.format(numero, hexadecimal))
else:
    print('Opção inválida, TENTE NOVAMENTE.')



