first = float(input('Primeira nota: '))
second = float(input('Segunda nota: '))
media = (first + second) / 2

print('Sua média é {:.1f}'.format(media))

if media < 5.0:
    print('\033[4;31mREPROVADO\033[m')
elif media <= 6.9:
    print('\033[33;4mRECUPERAÇÃO\033[m')
else:
    print('\033[32;4mAPROVADO\033[m')

