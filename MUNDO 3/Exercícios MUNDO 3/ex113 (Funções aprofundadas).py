def leiaint(num):
    while not num.isdigit():
        print('\033[31mERRO! Digite um número inteiro válido\033[m')
        num = (input('Digite um número inteiro: '))
    return  num

def leiafloat(num):
    try:
        num = float(num)
    except ValueError:
        while True:
            print('\033[31mERRO! Digite um número real válido\033[m')
            try:
                num = input('Digite um número real: ')
                num = float(num)
            except ValueError:
                print('\033[31mERRO! Digite um número real válido\033[m')
                num = input('Digite um número real: ')

            else:
                break
    except KeyboardInterrupt:
        print('\033[31mO usuário preferiu não mostrar dados.\033[m')
        num = 0
    return float(num)



#Programa principal

n1 = leiaint(input('Digite um número inteiro: '))
n2 = leiafloat(input('Digite um número real: '))
print(f'O número inteiro foi {n1} e número real foi {n2} ')