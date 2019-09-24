print('\033[32m-=-'*15)
print('Sequência de Fibonacci')
print('-=-'*15)
n = int(input('\033[mQuantos termos você quer mostrar? R:'))


t1 = 0
t2 = 1

print('{} {} '.format(t1, t2), end='')

count = 3
while count <= n:
    t3 = t2 + t1
    print('{} '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
# Fibonacci = t3 é a soma dos dois útimoss