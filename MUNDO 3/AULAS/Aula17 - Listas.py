lista = []

# Inserir novo elemento no final da lista
lista.append('elemento')

# Inserir novo elemento em qualquer posição
lista.insert(0, 'elemento')  #(posicao, elemento)

# Deletar elementos da lista
#Com posição do elemento
del lista[3]
lista.pop(3) #Geralmente usado para apagar o último elemento
#Com nome do elemento
lista.remove('nome_do_elemento')

if 'pizza' in lanche:
    lanche.remove('pizza')

####################################################

valores = list(range(4, 11))
valores.sort() #Colocar em ordem
valores.sort(reverse=True) #Ao contrário

###################################################
# LER VALORES ATRAVÉS DO TECLADO
valores = []
'''valores.append(3)
valores.append(2)
valores.append(5)'''

for cont in range (0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
######################################################
#VINCULO ENTRE LISTAS

a = [1,2,3,4]
b = a
####################################

# Criar copia entre listas
a = [1,2,3,4]
b = a[:] #receber todos os valores de a
