def aumentar(valor, porcent):
    percent = (valor / 100) * porcent
    final = valor + percent
    return final


def diminuir(valor, porcent):
    percent = (valor / 100) * porcent
    final = valor - percent
    return final


def metade(valor):
    n = valor / 2
    return n


def dobro(valor):
    n = valor * 2
    return n


def moeda(num):
    resp = f'R${num:.2f}'
    return resp
