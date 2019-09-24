
palavra = str(input('Digite uma frase:').replace(' ','').strip())
palavra = palavra.lower()
invertido = palavra[::-1]

if palavra == invertido:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digita NÃO é um palíndromo')