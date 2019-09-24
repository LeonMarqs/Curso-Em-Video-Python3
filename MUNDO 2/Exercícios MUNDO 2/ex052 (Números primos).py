n = int(input('Digite um número: '))
cont = 0
for c in range (1, n +1):
    if n % c == 0:
        print('\033[32m', end=' ')
        cont += 1 # aumenta em 1 a cada vez que for divisivel
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if cont == 2: #Se ele for divisivel apenas por dois numeros dentro do range
    print('\n\033[m O número É PRIMO')
else:
    print('\n\033[mO número NÃO É PRIMO')
