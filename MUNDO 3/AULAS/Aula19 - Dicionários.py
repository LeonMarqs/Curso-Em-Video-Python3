# Declarar um dicionário
'''dados = dict()'''
#dados = {}

####################
dados = {'nome':'João', 'idade':17, 'sexo':'masculino'}
dados1 = {'nome':'Maria', 'idade':18, 'sexo':'feminino'}
linha = '==' * 20
# Printar na tela
print(dados)
print(dados.items())
print(dados.values())
print(dados.keys())

print(linha)

print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])

################ para formatar, precisa de ASPAS DUPLAS ######################
print(f'O {dados["nome"]} tem {dados["idade"]} anos ')
print(linha)

# Adicionar uma nova key com valor
dados['cidade'] = 'Carapicuiba'
print(dados)
# Deletar alguma key com os valores dentro
del dados['cidade']
print(dados)
print(linha)
# Com FOR
for keys, values in dados.items():
    print(f'O {keys} é {values}')

print(linha)

#Dicionarios dentro de listas
pessoas = [dados, dados1]
''' Ou pessoas = []
pessoas.append(dados)
pessoas.append(dados1)
'''
print(pessoas)
print(pessoas[0]['nome'])
print(pessoas[0]['sexo'])
print(pessoas[1]['nome'])
print(pessoas[1]['idade'])
print(linha)
########################################################
estado = dict()
brasil = list()

for c in range(0 , 3):
    estado['Estado'] = str(input('Digite o estado: '))
    estado['Sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy()) # copiar os dados
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    for e in e.values():
        print(e, end=' ')
    print()