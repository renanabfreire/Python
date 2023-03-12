import ex108moeda

p = float(input('Digite o preço: R$'))
print(
    f'A metade de {ex108moeda.moeda(p)} é {ex108moeda.moeda(ex108moeda.metade(p))}')
print(
    f'O dobro de {ex108moeda.moeda(p)} é {ex108moeda.moeda(ex108moeda.dobro(p))}')
print(f'Aumentando 10%, temos {ex108moeda.moeda(ex108moeda.aumentar(p, 10))}')
