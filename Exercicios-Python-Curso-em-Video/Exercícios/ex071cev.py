q = 0
c = 50

print(30 * '=')
print('          BANCO RABF')
print(30 * '=')

v = int(input('Que valor você quer sacar? R$'))

while True:
    if v >= c:
        v -= c
        q += 1

    else:
        if q > 0:
            print(f'Total de {q} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        q = 0

        if v == 0:
            break

print(30 * '=')
print('Volte sempre ao BANCO RABF! Tenha um Bom Dia!')
