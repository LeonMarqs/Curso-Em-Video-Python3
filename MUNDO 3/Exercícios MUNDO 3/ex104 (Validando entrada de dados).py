def leiaint(num):
    while not num.isdigit():
        print('\033[31mERRO! Digite um número inteiro válido\033[m')
        num = (input('Digite um número inteiro: '))
    return  num


#Programa principal

n = leiaint(input('Digite um número inteiro: '))
print(f'Você acabou de digitar o número {n}')