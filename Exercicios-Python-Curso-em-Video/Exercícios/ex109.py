import ex109moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {ex109moeda.moeda(p)} é {ex109moeda.metade(p)}')
print(f'O dobro de {ex109moeda.moeda(p)} é {ex109moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {ex109moeda.aumentar(p, 10, True)}')
print(f'Diminuíndo 13%, temos {ex109moeda.diminuir(p, 13, True)}')
