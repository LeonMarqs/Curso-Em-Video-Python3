c = 'S'
lista = []

while c != 'N' and c == 'S':
    n = int(input('Digite um valor: '))
    lista += [n]
    c = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

qtd = len(lista)
media = sum(lista) / len(lista)
maior = max(lista)
menor = min(lista)

print('Você digitou {} números'.format(qtd))
print('O maior valor lido foi {}'.format(maior))
print('O menor valor lido foi {}'.format(menor))
print('A média dos valores lidos é de {:.2f}'.format(media))
