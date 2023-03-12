def notas(*n, sit=False):
    '''-> Função para analisar note=as e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma'''
    dici = dict()
    dici['total'] = len(n)
    dici['maior'] = max(n)
    dici['menor'] = min(n)
    dici['média'] = sum(n) / len(n)

    if sit:
        if dici['média'] < 5:
            dici['situação'] = 'RUIM'
        elif dici['média'] < 7:
            dici['situação'] = 'RAZOÁVEL'
        else:
            dici['situação'] = 'BOA'

    return dici


resp = notas(3.5, 2, 6.5, sit=True)
print('-'*30)
print(resp)
