pessoas = [['João', 15],['Maria', 22], ['Messias', 35]]
print(pessoas[0][1])
print(pessoas[1][0])
print(pessoas[2][1])
print(pessoas)
print(pessoas[1])
#############################################################

teste = list()
teste.append('Leonardo')
teste.append(17)
galera = list()
galera.append(teste[:])
teste[0]  = 'João'
teste[1] = 16
galera.append(teste[:])
print(galera)
##############################################################
galera = [['Leo',  17],['Kleberson', 18],['oaquem', 56]]

for p in  galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

##########################################################
galera2 = []
dado = []
menor = mai = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
for p in galera2:
    if p[1] >= 21:
        print(f'O(a) {p[0]} é maior de idade')
        mai += 1
    else:
        print(f'O(a) {p[0]} é menor de idade')
        menor += 1
print(f'{menor} menores e {mai} maiores')