import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Iniciar biblioteca do pygame
pygame.init()


def desenha(ctotal):
    for c in ctotal:
        pygame.draw.rect(tela, (0, 20, 220), (c[0], c[1], 20, 20))


def iniciar(move):  # configurações iniciais
    global pont, cX, cY, muv, mX, mY, corpocobra, esquerda, direita, baixo, cima
    # pontuação
    pont = 0

    # posição da cobra
    cX = 160
    cY = 240

    muv = move

    # posição da maçã
    mX = 480
    mY = 240

    # posições 0
    corpocobra = []
    esquerda = False
    direita = False
    baixo = False
    cima = False


# iniciar opções
iniciar(0)

# música de fundo
#fundo = pygame.mixer.music.load('Fundo.mp3')
# pygame.mixer.music.play(-1)

# configuração de texto
fonte = pygame.font.SysFont('timesnewroman', 20, False, True)
lfonte = pygame.font.SysFont('timesnewroman', 60, True, False)
rfonte = pygame.font.SysFont('timesnewroman', 15)
lmensagem = 'VOCÊ PERDEU'
rmensagem = 'Pressione <SPACE> para reiniciar'
creditos = 'Criador:'

# opções da tela
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jogo da Cobrinha')
relogio = pygame.time.Clock()

while True:
    relogio.tick(10)  # Taxa de frames
    tela.fill((50, 200, 100))  # Cor da tela
    mensagem = f'Pontuação: {pont}'
    texto = fonte.render(mensagem, False, (0, 0, 0))

    # eventos
    for event in pygame.event.get():
        if event.type == QUIT:  # fechar jogo
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # movimentação da cobra
            if event.key == K_UP:  # cima
                if cY == 2 or baixo == True:
                    pass
                else:
                    muv = 1
            if event.key == K_DOWN:  # baixo
                if muv == 1 or cima == True:
                    pass
                else:
                    muv = 2
            if event.key == K_RIGHT:  # direita
                if muv == 4 or esquerda == True:
                    pass
                else:
                    muv = 3
            if event.key == K_LEFT:  # esquerda
                if muv == 3 or direita == True:
                    pass
                else:
                    muv = 4

    # calculando tamanho da cobra
    if len(corpocobra) > pont+1:
        del corpocobra[0]

    # lista da posição atual
    cabecacobra = []
    cabecacobra.append(cX)
    cabecacobra.append(cY)

    if cabecacobra in corpocobra:
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))  # Cor da tela
            ltexto = lfonte.render(lmensagem, False, (0, 0, 0))
            rtexto = rfonte.render(rmensagem, False, (0, 0, 0))
            credito = rfonte.render(creditos, False, (0, 0, 0))
            instagram = rfonte.render(
                'Instagram: @renan_abf', False, (0, 0, 0))
            git = rfonte.render('github.com/renanabfreire', False, (0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        iniciar(3)
                        morreu = False

            tela.blit(instagram, (20, 430))
            tela.blit(git, (20, 460))
            tela.blit(credito, (20, 400))
            tela.blit(ltexto, (115, 100))
            tela.blit(rtexto, (210, 300))
            tela.blit(texto, (250, 210))
            pygame.display.update()

    # lista de posições
    corpocobra.append(cabecacobra)
    desenha(corpocobra)

    maca = pygame.draw.circle(tela, (220, 10, 0), (mX, mY), 8)
    cobra = pygame.draw.rect(tela, (0, 20, 220), (cX, cY, 20, 20))

    # atualização das posições
    if muv == 1:
        cima = True
        direita = False
        esquerda = False
        cY -= 20
    elif muv == 2:
        baixo = True
        direita = False
        esquerda = False
        cY += 20
    elif muv == 3:
        direita = True
        baixo = False
        cima = False
        cX += 20
    elif muv == 4:
        esquerda = True
        baixo = False
        cima = False
        cX -= 20

    # reposicionamento na tela
    if cX == 640:
        cX = 0
    elif cY == 480:
        cY = 0
    elif cX == -20:
        cX = 640
    elif cY == -20:
        cY = 480

    if cobra.colliderect(maca):  # colisão
        mX = randint(8, 632)
        mY = randint(8, 472)
        pont += 1

    # Texto da posição
    tela.blit(texto, (500, 20))

    pygame.display.update()
