primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
if primeiro > segundo:
    print('O \033[33;4m{} (primeiro valor)\033[m é maior'.format(primeiro))
elif primeiro < segundo:
    print('O \033[33;4m{} (segundo valor)\033[m é maior'.format(segundo))
else:
    print('Os dois valores são \033[33;4miguais\033[m')
