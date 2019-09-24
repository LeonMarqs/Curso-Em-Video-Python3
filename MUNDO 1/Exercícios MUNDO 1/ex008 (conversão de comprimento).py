#km  hm  dam  m  dm  cm  mm
print('\033[33m-=-'*12)
print('Conversor de metros')
print('-=-'*12)
m = float(input('\033[mDigite o valor em \033[34;4mmetros\033[m: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{}m = {}km\n{}m = {}hm\n{}m = {}dam\n{}m = {}dm\n{}m = {}cm\n{}m = {}mm'.format(m,km,m,hm,m,dam,m,dm,m,cm,m,mm))