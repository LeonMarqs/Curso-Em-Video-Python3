from datetime import  datetime
ano_atual = datetime.today().year

pessoa = {'nome': str(input('Nome: ')),
          'idade': int(input('Ano de nascimento: ')),
          'ctps': int(input('Carteira de trabalho (0 se não tem): '))
          }
pessoa['idade'] = ano_atual - pessoa['idade']

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    contribuicao = ano_atual - pessoa['contratação']
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35) - datetime.now().year

print('=='*20)

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
