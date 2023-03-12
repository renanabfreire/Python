def moeda(num):
    resp = f'R${num:.2f}'
    return resp


def aumentar(valor, porcent, formatar=False):
    percent = (valor / 100) * porcent
    final = valor + percent
    if formatar is True:
        final = moeda(final)
    return final


def diminuir(valor, porcent, formatar=False):
    percent = (valor / 100) * porcent
    final = valor - percent
    if formatar is True:
        final = moeda(final)
    return final


def metade(valor, formatar=False):
    n = valor / 2
    if formatar is True:
        n = moeda(n)
    return n


def dobro(valor, formatar=False):
    n = valor * 2
    if formatar is True:
        n = moeda(n)
    return n


def resumo(valor, aumento, diminuição):
    r = f"""{30 * '-'}\n{'RESUMO DO VALOR': ^30}\n{30 * '-'}
{'Preço analisado:':20}{moeda(valor)}
{'Dobro do preço:':20}{dobro(valor, True)}
{'Metade do preço:':20}{metade(valor, True)}
{f'{aumento}% de aumento:':20}{aumentar(valor, aumento, True)}
{f'{diminuição}% de redução:':20}{diminuir(valor, diminuição, True)}
{30 * '-'}"""

    return print(r)
