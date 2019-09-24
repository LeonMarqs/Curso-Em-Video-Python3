b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a  = (b*h)
t = a/2
print('A área da parede é {:.2f}m²\nA quantidade de tinta para pintar essa parede é de {:.1f} L'.format(a, t))
# Cada litro de tinta pinta uma área de 2m²