print('=='*20)
print('{:^40}'.format('BANCO DO LEONARDO'))
print('=='*20)

print('          Bem vindo ao BDL\n')
sacar = int(input('Quantos reais você quer sacar? R$'))
print('=='*20)

total = sacar

ced = 100
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break

print('=='*20)

''''cinquenta = 0
vinte = 0
dez = 0
um = 0

while sacar >= 50:
    cinquenta += 1
    sacar -= 50

while sacar >= 20:
    vinte += 1
    sacar -= 20

while sacar >= 10:
    dez += 1
    sacar -= 10

while sacar >= 1:
    um += 1
    sacar -= 1

print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')'''
