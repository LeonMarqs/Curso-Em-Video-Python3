frase = 'Curso em Vídeo Python'
#FATIAMENTO
print('FATIAMENTO')
print(frase[9:15])
print(frase[9:])
print(frase[:9])
print(frase[9::3])
print(frase[9:21:2])
print('--'*20)

#ANÁLISE
print('ANÁLISE')

print(len(frase),'caracteres') #caracteres
print('--'*20)

print(frase.count('o',0,13),'quantos >o< minusculos tem na frase') #quanras vezes exite a letra o na frase
                 #do 0 até o 13 (0 ao 12)

print('--'*20)
print(frase.find('Android')) #onde ele encontrou o 'deo'/se der -1 é porque não existe
print('--'*20)

print('Curso'in frase) # existe a palavra na frase?
print('--'*20)

#TRANSFORMAÇÃO
print('TRANSFORMAÇÃO')

print(frase.replace('Python','Android')) #Trocar a palavra por outra
print('--'*20)

print(frase.upper(),'......MAIÚSCULO')

print(frase.lower(),'......minúsculo')

print(frase.capitalize(),'......Capitalizado')

print(frase.title(),'......Todas As Palavras No Começo Maiúsculas')
print('--'*20)
frase2= '    Aprenda Python    '

print(frase2.strip(),'....Tirar os espaços inúteis')
print(frase2.rstrip(),'... tirar os espaços da direita (right)')
print(frase2.lstrip(),'...Tirar os espaços da esquerda (left)')
print('--'*20)

#DIVISÃO
print('DIVISÃO')

frase3 = 'Curso em Vídeo Python'

s = frase3.split()
print(''.join(s))

#TROCAR MAIUSCULO COM MINUSCULO
test = 'This is just a short string'
test.swapcase()
'tHIS IS JUST A SHORT STRING.'







