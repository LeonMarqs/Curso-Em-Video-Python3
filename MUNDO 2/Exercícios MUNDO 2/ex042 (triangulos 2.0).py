print('\033[33m-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
a = int(input('Digite o primeiro segmento: '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento:\033[m '))

calculo = a < (b + c) and b < (a + c) and c < (a + b)
equilatero = a == b == c
isosceles = a != c == b or b != c == a or c != b == a
escaleno = a != b != c != a

if calculo == True:
    print('\033[32;4mPodem formam um triângulo')
    if equilatero == True:
        print('Triangulo Equilátero')
    elif isosceles == True:
        print('Triangulo Isósceles')
    elif escaleno == True:
        print('Triangulo Escaleno')
else:
    print('\033[31;4mNÃO podem formar um triângulo')
