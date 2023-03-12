l = list()

for c in range(1, 8):
    l.append(int(input(f'Digite o {c}º valor: ')))

l.sort()

print('-=' * 30)
print('Os valores pares foram:', end=' ')
for v in l:
    if v % 2 == 0:
        print(v, end=' ')

print('\nOs valores ímpares foram:', end=' ')
for v in l:
    if v % 2 == 1:
        print(v, end=' ')
