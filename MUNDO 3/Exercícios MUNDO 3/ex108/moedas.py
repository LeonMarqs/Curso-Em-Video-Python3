def metade(n=0):
    return n / 2

def dobro(n=0):
    return n *2

def aumentar(n=0, p=0):
    por = n + (p/100 * n)
    return por

def diminuir(n=0, p=0):
    por = n - (p/100 * n)
    return por

def moeda(preco=0 , moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')