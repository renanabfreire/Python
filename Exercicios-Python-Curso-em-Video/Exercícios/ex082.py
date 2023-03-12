l = []
lp = []
li = []

while True:
    n = (int(input('Digite um valor: ')))

    l.append(n)
    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)

    o = ' '
    while o not in 'sn':
        o = input('Quer continuar? [S/N] ').strip().lower()[0]

    if o == 'n':
        break

print(15 * '-=')
print(f'A lista completa é {l}')
print(f'A lista de pares é {lp}')
print(f'A lista de impares é {li}')
