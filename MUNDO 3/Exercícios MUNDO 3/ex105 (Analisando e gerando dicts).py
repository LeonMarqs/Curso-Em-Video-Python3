def notas(*num, sit = False):

    """
    => Função que lê notas de um aluno e retorna informações
    :param num: Notas a serem lidas
    :param sit: (opcional) Mostra a sitiação do aluno em função da média
    :return: Um dicionário com as informações
    """

    media = sum(num) / len(num)
    informacoes = {'total':len(num),'maior':max(num),'menor':min(num),'média':media}
    if sit:
        if media < 5:
            informacoes['situação'] = 'RUIM'
        elif  5 < media < 7:
            informacoes['situação'] = 'BOA'
        else:
            informacoes['situação'] = 'ÓTIMA'
    return informacoes


resp = notas(10, 8, 5.2, 10, sit=True)
print(resp)
print('===='*20)
help(notas)