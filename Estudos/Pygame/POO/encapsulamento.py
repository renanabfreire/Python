"""
public, protected, private
_ public_
__ private (NOMECLASSE__nomeatributo)
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Renan')
bd.inserir_cliente(2, 'Eduarda')
bd.inserir_cliente(3, 'Caio')
bd.lista_clientes()
print()
bd.apaga_cliente(3)
bd.lista_clientes()
bd.__dados = 'Outra coisa'
print(bd.__dados)
bd.lista_clientes
print(bd._BaseDeDados__dados)

"""
__ permite que o elemento seja alterado apenas dentro
da classe, fora será criado outro
"""
