# crie um programa que leia o nome completo e mostre
#nome com letra maiuscula
#nome com letra minuscula
#quantas letras ao todo (sem considerar espaço)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
maius= nome.upper()
print('Seu nome em maiúsculo é {}'.format(maius))

minus= nome.lower()
print('Seu nome em minúsculo é {}'.format(minus))

aotodo= len(''.join(nome.split())) #ou len(nome) - nome.count(' ')
primeiro= nome.split()
primeiro = primeiro [0]
letrasPrimeiro= len(primeiro)

print('Seu nome ao todo tem {} letras'.format(aotodo))

print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro, letrasPrimeiro))