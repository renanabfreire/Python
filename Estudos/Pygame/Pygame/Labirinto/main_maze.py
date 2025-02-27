# -*- coding: utf-8 -*-
from time import sleep
from maze import Maze
from collections import deque

s = []  # Usar lista como pilha para DFS

maze_csv_path = "labirinto1.txt"  # Substitua pelo caminho correto
maze = Maze()

maze.load_from_csv(maze_csv_path)

# Exibir o labirinto
maze.run()
maze.init_player()

# Localize a posição inicial do jogador
s.append(maze.get_init_pos_player())

# Enquanto a pilha não estiver vazia
while len(s) != 0:
    sleep(0.01)
    pos = s.pop()  # Usar pop() para comportamento de pilha (DFS)

    # Se a posição tiver o prêmio no local então
    if maze.find_prize(pos):
        print("Prêmio encontrado!")
        break

    # Mova o jogador para este local se for possível
    if maze.is_free(pos):
        maze.mov_player(pos)

        # Examine se as casas adjacentes estão livres e insira na pilha
        if maze.is_free((pos[0] + 1, pos[1])):
            s.append((pos[0] + 1, pos[1]))
        if maze.is_free((pos[0] - 1, pos[1])):
            s.append((pos[0] - 1, pos[1]))
        if maze.is_free((pos[0], pos[1] + 1)):
            s.append((pos[0], pos[1] + 1))
        if maze.is_free((pos[0], pos[1] - 1)):
            s.append((pos[0], pos[1] - 1))

print("Busca finalizada")
