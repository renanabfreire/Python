dp = list()
pM = pm = c = 0
ppM = list()
ppm = list()

while True:
    dp.append(input('Nome: '))
    dp.append(int(input('Peso: ')))

    if dp[1] > pM:
        pM = dp[1]
        ppM.clear()
        ppM.append(dp[0])
    elif dp[1] == pM:
        ppM.append(dp[0])

    if dp[1] < pm or pm == 0:
        pm = dp[1]
        ppm.clear()
        ppm.append(dp[0])
    elif dp[1] == pm:
        ppm.append(dp[0])

    dp.clear()
    c += 1

    o = ' '
    while o not in 'sn':
        o = input('Quer continuar? [S/N] ').lower().strip()[0]
    if o == 'n':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {c} pessoas.')
print(f'O maior peso foi de {pM:.1f}Kg. Peso de {ppM}')
print(f'O menor peso foi de {pm:.1f}Kg. Peso de {ppm}')
