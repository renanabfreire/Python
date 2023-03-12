from classes import ListaDeCompras, Produto

# produtos de uma loja
p1 = Produto('Livro da estante A', 10)
p2 = Produto('Livro da estante B', 15)
p3 = Produto('Conjunto de cartas', 40)
p4 = Produto('Boné', 30)
p5 = Produto('Óculos', 20)

l1 = ListaDeCompras()
l1.adicionar_produto(p2)
l1.adicionar_produto(p2)
l1.adicionar_produto(p5)

l1.lista_de_produtos()
l1.valor_total()

print()  # dividindo simulações

l2 = ListaDeCompras()
l2.adicionar_produto(p1)
l2.adicionar_produto(p3)
l2.adicionar_produto(p5)

l2.lista_de_produtos()
l2.valor_total()
