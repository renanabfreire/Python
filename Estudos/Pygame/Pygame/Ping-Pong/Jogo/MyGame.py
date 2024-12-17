# Importando bibliotecas
import pygame
from pygame.locals import *
from sys import exit

p1 = input('Player 1: ')
p2 = input('Player 2: ')

# Inicializando programa
pygame.init()

# Tela
largura = 640
altura = 480

# Bola
# Posição
pbx = 320
pby = 240
# Velocidade
vbx = 5
vby = 2
# Play
inicio = False

# Player 1
p1y = 190
pontuacaovermelho = 0

# Player 2
p2y = 190
pontuacaoazul = 0

tela = pygame.display.set_mode((largura, altura))  # Local do jogo
pygame.display.set_caption('My Game')  # Título
fps = pygame.time.Clock()  # Relógio

# Programa principal
while True:
    fps.tick(30)  # Taxa de fps
    tela.fill((0, 0, 0))  # Cor de fundo

    # Encerramento
    for event in pygame.event.get():
        if event.type == QUIT:
            print(f'O placar final foi {pontuacaovermelho}x{pontuacaoazul}')
            if pontuacaovermelho > pontuacaoazul:
                print(f'{p1} venceu')
            elif pontuacaovermelho < pontuacaoazul:
                print(f'{p2} venceu!')
            else:
                print('Foi um empate!')
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:  # Iniciando jogo
                inicio = True

    # Movendo Player 2
    if pygame.key.get_pressed()[K_UP]:
        p2y -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        p2y += 5

    # Movendo Player 1
    if pygame.key.get_pressed()[K_w]:
        p1y -= 5
    if pygame.key.get_pressed()[K_s]:
        p1y += 5

    # Desenhos
    # Cenário
    pygame.draw.line(tela, (255, 255, 255), (320, 10), (320, 470), 3)
    pygame.draw.line(tela, (255, 255, 255), (10, 10), (630, 10), 3)
    pygame.draw.line(tela, (255, 255, 255), (10, 470), (630, 470), 3)
    # Objetos
    player1 = pygame.draw.rect(
        tela, (255, 0, 0), (10, p1y, 10, 100))  # Player 1
    player2 = pygame.draw.rect(
        tela, (0, 0, 255), (620, p2y, 10, 100))  # Player 2
    bola = pygame.draw.circle(tela, (255, 0, 255), (pbx, pby), 10)  # Bola

    # Movimentação da bola
    if inicio == True:
        pbx += vbx
        pby += vby

    # Interação da bola com a parede
    if pby >= 460 or pby <= 20:
        vby *= -1

    if pbx >= 640:
        pontuacaovermelho += 1
    if pbx <= 0:
        pontuacaoazul += 1

    # Reiniciando jogo
    if pbx >= 640 or pbx <= 0:
        if pbx <= 0:
            vbx = -5
        elif pbx >= 640:
            vbx = 5
        pbx = 320
        pby = 240
        vby = 2

        inicio = False
        print(f'{p1}: {pontuacaovermelho}\n{p2}: {pontuacaoazul}')

    # Criando interação da bola com jogadores
    if pbx >= 610 and pby > (p2y - 10) and pby < (p2y + 110):  # Player 2
        vbx *= -1.1
        vby *= 1.1

    if pbx <= 30 and pby > (p1y - 10) and pby < (p1y + 110):  # Player 2
        vbx *= -1.1
        vby *= 1.1

    # Atualização do display
    pygame.display.update()
