print('-=-'* 10)
print('Múltiplos de 3')
print('-=-'* 10)

s = 0
cont = 0
for c in range (1, 501, 2):
    if (c % 3 == 0):
        s += c
        cont += 1
print('A soma dos {} números múltiplos de 3 é {}.'.format(cont, s))

