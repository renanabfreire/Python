l = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > max(l):
        l.append(n)
        print('Adicionado ao final da lista...')
    elif n < min(l):
        l.insert(0, n)
        print('Adicionado ao início da lista...')
    elif l[0] < n < l[1]:
        l.insert(1, n)
        print('Adicionado na posição 1 da lista...')
    elif l[1] < n < l[2]:
        l.insert(2, n)
        print('Adicionado na posição 2 da lista...')
    elif l[2] < n < l[3]:
        l.insert(3, n)
        print('Adicionado na posição 3 da lista...')

print('-=' * 15)
print(f'Os valores digitados foram em ordem foram {l}')
