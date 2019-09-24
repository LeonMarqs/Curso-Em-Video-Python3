print('-=-'* 10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'* 10)

t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 10
count = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while count <= total:
        print(t1, end= ' ')
        t1 += razao
        count += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais? R:'))


print('Foram mostrados {} termos'.format(total))






