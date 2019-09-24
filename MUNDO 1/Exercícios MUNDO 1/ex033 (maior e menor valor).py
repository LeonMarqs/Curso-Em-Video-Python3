a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))