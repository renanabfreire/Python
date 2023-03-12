# Criando variáveis
jogadores = []
jogador = {}
gols = []
jogo = 0

# Recebendo dados
while True:
    # Limpando variáveis
    jogador.clear()
    gols.clear()

    jogador['nome'] = input('Nome do jogador: ')

    elefante = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, elefante):  # Obtendo valores dos jogos
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    # Adicionando jogador a lista
    jogadores.append(jogador.copy())

    # Encerrando a repetição
    o = ' '
    while o not in 'sn':
        o = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if o == 'n':
        break

# Apresentando valores
print('-=' * 30)

# Tabela para organização
print(f'{"Nº":4}{"Nome":15}{"Gols":15}{"Total"}',)
print('-' * 60)
for i, c in enumerate(jogadores):
    print(f'{i+1:0>3}', end=' ')
    for d in c.values():
        print(f'{str(d):15}', end=' ')
    print()

# Especificando jogador
n = -1
while True:
    print('-' * 60)
    n = int(input('Mostrar dados de qual jogador? [0 encerra] '))
    n -= 1
    if n == -1:
        break
    if n > len(jogadores) or n < 0:
        print(f'ERRO, não existe jogador com código {n}! Tente novamente.')
    else:
        print(f'== Levantamento do jogador {jogadores[n]["nome"]}:')
        for c in gols:
            jogo += 1
            print(f'    => Na partida {jogo}, fez {c} gols.')
