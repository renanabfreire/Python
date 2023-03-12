from random import randint

l = []
cont = 0

print(30 * '-')
print(f'{"JOGA NA MEGA SENA":^30}')
print(30 * '-')

n = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'Sorteando {n} jogos', '=-' * 3)

for c in range(0, n):
    while True:
        num = randint(1, 60)
        if num not in l:
            l.append(num)
            cont += 1
        if cont == 6:
            break

    l.sort()

    print(f'Jogo {c + 1}: {l}')

    l.clear()

print('-=' * 3, '< BOA SORTE! >' '=-' * 3)
