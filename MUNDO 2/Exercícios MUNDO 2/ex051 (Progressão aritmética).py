print('-=-'* 10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'* 10)

termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a  razão da PA: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + 1, razao):
    print(c, end='. ')