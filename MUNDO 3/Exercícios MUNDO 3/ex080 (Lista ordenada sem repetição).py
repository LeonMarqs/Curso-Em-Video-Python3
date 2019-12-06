valores = []
maior = 0
menor = 0
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        print('Adicionado no final da lista')
        valores.append(n)

    else:
        pos = 0
        while  pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
        print(f'Adicionado na posição {valores.index(n)} da lista.')
print(valores)
