print('-=-'*20)
n = int(input('Digite um número qualquer: '))
print('-=-'*20)
calculadora =  n % 2
if calculadora == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número é ÍMPAR')