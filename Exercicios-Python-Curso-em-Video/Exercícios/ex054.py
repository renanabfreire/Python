from datetime import date

a = date.today().year
m = 0
M = 0

for c in range(1, 8):
    n = int(input(f'Ano de nascimento {c}: '))
    if (a - n) < 21:
        m += 1
    else:
        M += 1

print(f'{m} são de menor e {M} são de maior.')
