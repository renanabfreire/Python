class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - self.preco * percentual / 100

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

p1 = Produto('jogo', 100)
print(p1.nome, p1.preco)
print(p1.desconto(10))
