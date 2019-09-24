cont = 0
soma = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
       soma += n
       cont += 1
print('A soma dos números {} pares é de {}'.format(cont, soma))
