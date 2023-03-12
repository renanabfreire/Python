from sistema.interface import escrever


def existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    open(nome, 'wt+')


def ler(nome):
    a = open(nome, 'rt')
    for l in a:
        pessoa = l.split(';')
        pessoa[1] = pessoa[1].replace('\n', '')
        print(f'{pessoa[0]:<30}{pessoa[1]:>3}')


def cadastrar(arquivo, nome, idade):
    a = open(arquivo, 'at')
    a.write(f'{nome};{idade}\n')
