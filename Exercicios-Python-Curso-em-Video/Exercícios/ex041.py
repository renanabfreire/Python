from datetime import date

d = date.today().year

print(8 * '=' + 'DESCOBRIR CATEGORIA' + 8 * '=')

a = int(input('Digite em que ano você nasceu para descobrir sua categoria: '))

i = d - a

if i < 10:
    c = 'Mirim'
elif i < 15:
    c = 'Infantil'
elif i < 20:
    c = 'Junior'
elif i < 21:
    c = 'Sênior'
else:
    c = 'Master'

print(f'Sua categoria é {c}')
