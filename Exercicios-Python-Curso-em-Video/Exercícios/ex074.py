from random import randint

a = 0
b = 0
c = 0
d = 0
e = 0

for cont in range(0, 5):
    e = randint(0, 9)

    if cont == 0:
        d = e
    elif cont == 1:
        c = e
    elif cont == 2:
        b = e
    elif cont == 3:
        a = e

    tupla = a, b, c, d, e

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')
