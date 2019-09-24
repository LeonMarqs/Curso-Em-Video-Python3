from datetime import date
print('-=-'*23)
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
print('-=-'*23)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))

