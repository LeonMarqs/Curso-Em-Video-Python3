from datetime import date
gen = int(input('''Você é:
[1] HOMEM
[2] MULHER
: '''))
if gen == 2:
    print('Você não precisa se alistar')
elif gen == 1:
    ano = int(input('Informe seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano

    print('Quem nasceu em {} tem {} anos de idade em {}'.format(ano, idade, atual))
    if idade > 18:
        print('Já passou {} ano(s) para se alistar'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(ano + 18))
    elif idade < 18:
        print('Falta {} ano(s) pra você se alistar'.format(18 - idade))
        print('Seu alistamento será em {}'.format(18 - idade + atual))
    else:
        print('Você precisa se alistar AGORA')
else:
    print('Número incorreto, TENTE  NOVAMENTE.')
