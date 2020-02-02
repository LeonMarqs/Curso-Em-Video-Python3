def metade(n=0, form = False):
    if form:
        return f'R${n/2:.2f}'.replace('.', ',')
    else:
        return n / 2

def dobro(n=0, form = False):
    if form:
        return f'R${n*2:.2f}'.replace('.', ',')
    else:
        return n * 2

def aumentar(n=0, p=0, form = False):
    por = n + (p/100 * n)
    if form:
        return f'R${por:.2f}'.replace('.', ',')
    else:
        return por

def diminuir(n=0, p=0, form = False):
    por = n - (p/100 * n)
    if form:
        return f'R${por:.2f}'.replace('.', ',')
    else:
        return por

def moeda(preco=0 , moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

