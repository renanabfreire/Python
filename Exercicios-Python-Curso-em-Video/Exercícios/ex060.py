m = 1

print('Cálculo de fatorial')
n = int(input('Digite o valor desejado: '))

if n == 0:
    print('Valor igual a 0')
else:
    print(f'Fatorial de {n}', end=' ')

while n != 0:
    m *= n
    n -= 1

print(f'igual a {m}.')
