maiores = homens = mul20 = 0

while True:
    print('--' * 10)
    print('CADASTRE UMA PESSOA')
    print('--' * 10)
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mul20 += 1

    continuar = ' '
    while continuar not in 'SN':
        print('--'*10)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Ao todo são {maiores} \033[33mmaior(es) de idade\033[m.')
print(f'{mul20} mulheres com \033[33mmenos de 20 anos\033[m.')
print(f'{homens} \033[33mhomem(s)\033[m.')