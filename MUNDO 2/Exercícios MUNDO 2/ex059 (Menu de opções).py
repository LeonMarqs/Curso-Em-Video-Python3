from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

escolha = 0
while escolha != 5:
    escolha = int(input('\033[mDigite a opção desejada:\n\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n\033[35m'))
    if escolha == 1:
        somar = n1 + n2
        print('A soma entre {} + {} = {}\n'.format(n1, n2, somar))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} = {}\n'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            print('{} é > que {}'.format(n1, n2))
        if n2 > n1:
            print('{} é > que {}'.format(n2, n1))
        else:
            print('Os dois valores são iguais')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha != 5:
        print('Opção inválida, tente novamente... ')
    sleep(2)
    print('-=-'*10)

print('Fim do programa, volte sempre!')

