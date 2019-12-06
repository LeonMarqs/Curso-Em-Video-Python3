def linha():
    print('=='*20)
#################################################
# Função com parâmetro
def mensagem(msg):
    print('--'*20)
    print(msg)
    print('--'*20)
# Printar com o parâmetro
mensagem('Leonardo é legal')
mensagem('João é chato')

############################################

def soma1 (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma vale {s}')
    print()
    linha()


soma1(a=2, b=4)
soma1(b=2, a=5)
soma1(1, 7)
soma1 ('2','a')
###########################################################################################

'''COLOCAR VÁRIOS PARÂMETROS'''
'''TUPLAS'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')


contador(1, 2, 4)
contador(3, 6)
contador(2, 3, 5, 7, 9, 3)
linha()

def soma2(*nums):
    s = 0
    for n in nums:
        s += n
    print(f'Somando os valores {nums} temos {s}')


soma2(2, 4, 5, 6)
soma2(4, 5)
soma2(4, 7, 3)
linha()

#########################################################################


'''       LISTAS     '''

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *=2
        pos += 1


valores = [7, 2, 5, 8]
print(valores)

dobra(valores)
print(valores)