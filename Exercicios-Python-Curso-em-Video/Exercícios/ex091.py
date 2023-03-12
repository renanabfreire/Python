from random import randint

jogos = {}
jogoordenado = {}
ordem = []
cont = 1

for c in range(1, 5):
    n = randint(1, 6)

    jogos[f'Jogador {c}'] = n
    ordem.append(n)

ordem.sort(reverse=True)

for c in ordem:
    for a, b in jogos.items():
        if b == c:
            jogoordenado[a] = b

print('Valores sorteador:')
for i, c in jogos.items():
    print(f'o {i} tirou {c}')

print('Ranking dos jogadores: ')
for i, c in jogoordenado.items():
    print(f'{cont}º lugar: {i} com {c}')
