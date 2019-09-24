print('Tres aspas duplas')
print('--'*20)
print("""Sublime Text é um editor de texto e código-fonte multiplataforma,
escrito em linguagem C++, que foi inicialmente pensado para ser uma extensão
do vim. Este editor oferece recursos extraordinários e um desempenho simplesmente
surpreendente. Uma das características mais fantásticas deste editor é a função 
“multi-caret editing” que permite escrever a mesma coisa em diversos sítios.""")
                #três aspas duplas printam um texto grande
print('--'*20)

frase = 'Curso em Vídeo Python'

print(frase.upper().count('O'))
print('--'*20)

print(frase.replace('o','a'))
print('--'*20)

dividido = frase.split()
print(dividido[2][3]) #mostrar a letra da posição  3 da lista 2