from math import trunc

d = float(input('Digite a distância em km: '))

if d <= 200:
    trunc(d)
    print('A sua viagem custaré R${:.2f}'.format(d * 0.50))
else:
    trunc(d)
    print('A sua viagem custará R${:.2f}'.format(d * 0.45))
