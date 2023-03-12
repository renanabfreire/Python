lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livros', 34.9)

print(39 * '=')
print(f'{"VALOR DE PRODUTOS":^39}')
print(39 * '=')

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='R$')
    if c % 2 == 1:
        print(f'{lista[c]:>7.2f}')
