sexo = str(input('Digite seu sexo \033[35m[M/F]\033[m: ')).upper().strip() #[0] pegar só a primeira letra

homem = ['HOMEM','MASCULINO','MOÇO','MENINO','M']
mulher = ['MULHER','FEMININO','MOÇA','MENINA','F']

while sexo not in homem and sexo not in mulher :
    sexo = str(input('Digite novamente \033[35m[M/F]\033[m: ')).upper().strip()
if sexo in mulher:
    print('Certo, você é uma \033[31;4mmulher\033[m!')
else:
    print('Certo, você é um \033[34;4mhomem\033[m!')
print('ACABOU')
