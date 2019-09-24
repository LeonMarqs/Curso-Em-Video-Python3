while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('==='*15)
    if tabuada < 0:
        print('FIM DO PROGRAMA, VOLTE SEMPRE!')
        break
    for c in range (1, 11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('==='*15)
