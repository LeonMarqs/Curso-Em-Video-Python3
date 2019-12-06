def fatorial(n=1, show = False):

    '''
    => Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcional) Mostras ou não a conta
    :return: O valor de um número n
    '''

    f = 1
    for c in range (n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f


print(fatorial(3, True))
help(fatorial)
