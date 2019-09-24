print('-=-'* 10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'* 10)

t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 10
count = 1
while count <= n:
    print(t1, end= ' ')
    t1 += razao
    count += 1