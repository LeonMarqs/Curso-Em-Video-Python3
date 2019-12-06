from time import sleep

def linha():
    print('=='*15)


def area(lar, comp):
    area_terreno = lar * comp
    print('CALCULANDO...')
    sleep(1)
    print(f'A área de um terreno {lar}x{comp} é de {area_terreno}m²')


print('Controle de Terrenos')
linha()
area(lar=float(input('LARGURA(m): ')), comp=float(input('COMPRIMENTO(m): ')))

