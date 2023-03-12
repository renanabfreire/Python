def ficha(nome='<desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print(30*'-')
n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
ficha(n, g)
