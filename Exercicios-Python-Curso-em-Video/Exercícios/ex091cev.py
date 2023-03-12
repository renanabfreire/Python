# Importando módulos
from random import randint  # Geração d valor aleatório
from time import sleep  # Pausa entre valores
from operator import itemgetter  # Receber valor do dicionário

# Criando dicionário
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()  # Após ordenação de valores, o dicionário assume lista

print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
