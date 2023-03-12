q = 0
M = 0
m = 0

for c in range(1, 6):
    p = float(input(f'Peso {c}: '))
    if p > q:
        M = p
    elif q > p:
        m = p

    q = p

print(f'O maior é {M} e o menor é {m}')
