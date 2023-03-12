l = [[], [], [], [], [], [], [], [], []]
p = [[0, 0], [0, 1], [0, 2],
     [1, 0], [1, 1], [1, 2],
     [2, 0], [2, 1], [2, 2]]

for c in range(0, 9):
    l[c].append(int(input(f'Digite um valor {p[c]} ')))

print('-=' * 30)
for c in range(1, 10):
    print(f'{l[c - 1]:^3}', end=' ')
    if c % 3 == 0:
        print()
