l = []
n = 6

for c in range(0, 5):
    l.append(int(input(f'Digite um valor para a posição {c}: ')))

print(20 * '=-')

print(f'Você digitou os valores {l}')

print(f'O maior valor digitado foi {max(l)} nas posições', end=' ')

for c in range(0, 5):
    if max(l) in l[c:] and n != l.index(max(l), c):
        n = l.index(max(l), c)
        print(n, end=' ')

print(f'\nO menor valor digitado foi {min(l)} nas posições', end=' ')

for c in range(0, 5):
    if min(l) in l[c:] and n != l.index(min(l), c):
        n = l.index(min(l), c)
        print(n, end=' ')
