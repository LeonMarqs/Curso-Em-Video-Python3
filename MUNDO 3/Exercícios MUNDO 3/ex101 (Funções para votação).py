from datetime import datetime

ano_atual = datetime.today().year

def voto(n):
  if n < 16:
      status = 'NÃO PERMITIDO'
  elif n in [16, 17] or n >= 65:
      status = 'OPCIONAL'
  else:
      status = 'OBRIGATÓRIO'
  return status


pessoa = int(input('Ano de nascimento: '))
idade = ano_atual - pessoa

print(f'Com {idade} anos: VOTO {voto(idade)}')
