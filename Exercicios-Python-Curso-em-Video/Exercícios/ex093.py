# Criando variáveis
jogador = {}
gols = []
jogo = 0

# Recebendo dados
jogador['nome'] = input('Nome do jogador: ')

elefante = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, elefante):  # Obtendo valores dos jogos
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

# Apresentando valores
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {elefante} partidas.')
for c in gols:
    jogo += 1
    print(f'    => Na partida {jogo}, fez {c} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
