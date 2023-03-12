dp = []
l = []
mai = men = 0

while True:
    dp.append(input('Nome: '))
    dp.append(float(input('Peso: ')))

    if len(l) == 0:
        mai = men = dp[1]
    else:
        if dp[1] > mai:
            mai = dp[1]
        if dp[1] < men:
            men = dp[1]

    l.append(dp[:])
    dp.clear()

    o = ' '
    while o not in 'sn':
        o = input('Quer continuar? [S/N] ').strip().lower()[0]

    if o == 'n':
        break

print('-=' * 30)
print(f'Os dados foram {l}')
print(f'Ao todo, você cadastrou {len(l)} pessoas.')
print(f'O maior peso foi de {mai}Kg.', end=' ')
for p in l:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso foi de {men}.')
for p in l:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
