l = [[], [], [], [], [], [], [], [], []]
p = [[0, 0], [0, 1], [0, 2],
     [1, 0], [1, 1], [1, 2],
     [2, 0], [2, 1], [2, 2]]
somapar = somaterceira = maiorsegunda = 0

for c in range(0, 9):
    n = int(input(f'Digite um valor {p[c]} '))
    l[c].append(n)

    if 2 < c < 6:
        if c == 3 or n > maiorsegunda:
            maiorsegunda = n
    if n % 2 == 0:
        somapar += n
    if (c + 1) % 3 == 0:
        somaterceira += n

print('-=' * 30)
for c in range(1, 10):
    print(l[c - 1], end=' ')
    if c % 3 == 0:
        print()

print('-=' * 30)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maiorsegunda}.')
