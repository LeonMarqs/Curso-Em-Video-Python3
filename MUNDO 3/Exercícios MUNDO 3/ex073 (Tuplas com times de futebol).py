times = ('Santos','Palmeiras','Flamengo','Atlético','São Paulo','Internacional','Corinthians','Athletico-PR','Botafogo',
         'Bahia','Ceará SC','Goiás','Grêmio','Fortaleza','Vasco da Gama','Fluminense','Cruzeiro','Chapecoense','CSA','Avaí')

print('\033[32mOs cinco primeiros colocados são:\033[m')
for c in range (0, 5):
    print(f'{c+1}-{times[c]}')

print('\033[32m\nOs quatro útimos colocados são:\033[m')
pos = -1
posn = 20
for i in range (0, 5):
    print(f'{posn}-{times[pos]}')
    pos -= 1
    posn -= 1

print('\033[32m\nTimes em ordem alfabética:\033[m')
timesOrdem= sorted(times)
for a in range (0, len(times)):
    print(f'{timesOrdem[a]}')
pos = times.index('Chapecoense') + 1
print(f'\033[32m\nChapecoense está na {pos} posição\033[m')