import ex107moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {ex107moeda.metade(p)}')
print(f'O dobro de {p} é {ex107moeda.dobro(p)}')
print(f'Aumentando 10%, temos {ex107moeda.aumentar(p, 10)}')
print(f'Diminuíndo 13%, temos {ex107moeda.diminuir(p, 13)}')
