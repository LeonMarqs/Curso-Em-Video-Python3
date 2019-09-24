soma = count = 0

while True:
    n = int(input('Digite um número [999 para somar]: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'A soma dos {count} valores é de {soma}')
