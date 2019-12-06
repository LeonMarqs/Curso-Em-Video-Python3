#INTERACTIVE HELP

'''help()
print(input.__doc__)'''



#PARAMETROS OPCIONAIS
#DOCSTRINGS

def soma(a=0, b=0, c=0):

    """
    => Faz uma soma com três parâmetros
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Leonardo Marques
    """

    s = a + b + c
    print(f'A soma vale {s}')

help(soma)
soma(3, 2)

# ESCOPO DE VARIAVEIS
'''global a'''

# RETORNAR VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 4, 6)
r2 = somar(3, 4)
r3 = somar(4)

print(f'A soma vale {r1}, {r2} e {r3}')
############################### PRÁTICA ##################################
print('=='*20)
def fatorial(n=1):
    f = 1
    for c in range (n, 0, -1):
        f *= c
    return f

num =  int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial(num)}')

###############################################################
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número:'))
if par(num):
    print('É par')
else:
    print('Não é par')