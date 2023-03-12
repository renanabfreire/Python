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
