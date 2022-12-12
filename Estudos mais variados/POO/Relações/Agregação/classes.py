class ListaDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, Produto):
        self.produtos.append(Produto)

    def lista_de_produtos(self):
        for Produto in self.produtos:
            print(Produto.nome, Produto.valor)

    def valor_total(self):
        f = 0
        for Produto in self.produtos:
            f += Produto.valor
        print(f'A compra resultou num total de R${f}')


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
