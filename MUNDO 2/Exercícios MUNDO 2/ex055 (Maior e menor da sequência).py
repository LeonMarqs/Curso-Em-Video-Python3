maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('\033[35mPeso da {} pessoa:\033[m '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\033[32mO maior valor lido foi de {}Kg\033[m'.format(maior))
print('\033[31mO menor valor lido foi de {}Kg\033[m'.format(menor))