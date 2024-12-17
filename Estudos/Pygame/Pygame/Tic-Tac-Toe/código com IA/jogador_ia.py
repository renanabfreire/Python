# -*- coding: utf-8 -*-
from random import randint
from random import choice

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        # r1: Se você ou seu oponente tiver duas marcações em sequência, marque o quadrado restante.
        for i in range(0, 3):
            cont = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            for j in range(0, 3):
                if self.matriz[i][j] == Tabuleiro.JOGADOR_0:
                    cont += 1
                elif self.matriz[i][j] == Tabuleiro.JOGADOR_X:
                    cont += 4
                if self.matriz[j][i] == Tabuleiro.JOGADOR_0:
                    cont2 += 1
                elif self.matriz[j][i] == Tabuleiro.JOGADOR_X:
                    cont2 += 4
                if self.matriz[j][j] == Tabuleiro.JOGADOR_0:
                    cont3 += 1
                elif self.matriz[j][j] == Tabuleiro.JOGADOR_X:
                    cont3 += 4
                if self.matriz[j][2-j] == Tabuleiro.JOGADOR_0:
                    cont4 += 1
                elif self.matriz[j][2-j] == Tabuleiro.JOGADOR_X:
                    cont4 += 4

            # Vencer o jogo
            if cont == 2: # linha
                for c in range(0, 3):
                    if self.matriz[i][c] == Tabuleiro.DESCONHECIDO:
                        return (i, c)
            if cont2 == 2: # coluna
                for c in range(0, 3):
                    if self.matriz[c][i] == Tabuleiro.DESCONHECIDO:
                        return (c, i)
            if cont3 == 2: # diagonal principal
                for c in range(0, 3):
                    if self.matriz[c][c] == Tabuleiro.DESCONHECIDO:
                        return (c, c)
            if cont4 == 2: # diagonal secundária
                for c in range(0, 3):
                    if self.matriz[c][2-c] == Tabuleiro.DESCONHECIDO:
                        return (c, 2-c)
        for i in range(0, 3): 
            cont = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            for j in range(0, 3):
                if self.matriz[i][j] == Tabuleiro.JOGADOR_0:
                    cont += 1
                elif self.matriz[i][j] == Tabuleiro.JOGADOR_X:
                    cont += 4
                if self.matriz[j][i] == Tabuleiro.JOGADOR_0:
                    cont2 += 1
                elif self.matriz[j][i] == Tabuleiro.JOGADOR_X:
                    cont2 += 4
                if self.matriz[j][j] == Tabuleiro.JOGADOR_0:
                    cont3 += 1
                elif self.matriz[j][j] == Tabuleiro.JOGADOR_X:
                    cont3 += 4
                if self.matriz[j][2-j] == Tabuleiro.JOGADOR_0:
                    cont4 += 1
                elif self.matriz[j][2-j] == Tabuleiro.JOGADOR_X:
                    cont4 += 4

            # Bloquear jogador
            if cont == 8:  # linha
                for c in range(0, 3):
                    if self.matriz[i][c] == Tabuleiro.DESCONHECIDO:
                        return (i, c)
            if cont2 == 8:  # coluna
                for c in range(0, 3):
                    if self.matriz[c][i] == Tabuleiro.DESCONHECIDO:
                        return (c, i)
            if cont3 == 8:  # diagonal principal
                for c in range(0, 3):
                    if self.matriz[c][c] == Tabuleiro.DESCONHECIDO:
                        return (c, c)
            if cont4 == 8:  # diagonal secundária
                for c in range(0, 3):
                    if self.matriz[c][2-c] == Tabuleiro.DESCONHECIDO:
                        return (c, 2-c)

        # r2: Se houver uma jogada que crie duas sequências de duas marcações, use-a
        for i in range(0, 3):
            for j in range(0, 3):
                linha = 0
                coluna = 0
                dprincipal = 0
                dseecundaria = 0
                if self.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                    for c in range(1, i+1):
                        if self.matriz[i-c][j] == Tabuleiro.JOGADOR_0:
                            linha += 1
                        if self.matriz[i-c][j] == Tabuleiro.JOGADOR_X:
                            linha += 4
                    for c in range(1, 3-i):
                        if self.matriz[i+c][j] == Tabuleiro.JOGADOR_0:
                            linha += 1
                        if self.matriz[i+c][j] == Tabuleiro.JOGADOR_X:
                            linha += 4
                    for c in range(1, j+1):
                        if self.matriz[i][j-c] == Tabuleiro.JOGADOR_0:
                            coluna += 1
                        if self.matriz[i][j-c] == Tabuleiro.JOGADOR_X:
                            coluna += 4
                    for c in range(1, 3-j):
                        if self.matriz[i][j+c] == Tabuleiro.JOGADOR_0:
                            coluna += 1
                        if self.matriz[i][j+c] == Tabuleiro.JOGADOR_X:
                            coluna += 4
                    if i == j:
                        for c in range(1, i+1):
                            if self.matriz[i-c][j-c] == Tabuleiro.JOGADOR_0:
                                dprincipal += 1
                            if self.matriz[i-c][j-c] == Tabuleiro.JOGADOR_X:
                                dprincipal += 4
                        for c in range(1, 3-i):
                            if self.matriz[i+c][j+c] == Tabuleiro.JOGADOR_0:
                                dprincipal += 1
                            if self.matriz[i+c][j+c] == Tabuleiro.JOGADOR_X:
                                dprincipal += 4
                    if i == j+2 or i == j-2 or (i==1 and j==1):
                        for c in range(1, i+1):
                            if self.matriz[i-c][j+c] == Tabuleiro.JOGADOR_0:
                                dseecundaria += 1
                            if self.matriz[i-c][j+c] == Tabuleiro.JOGADOR_X:
                                dseecundaria += 4
                        for c in range(1, 3-i):
                            if self.matriz[i+c][j-c] == Tabuleiro.JOGADOR_0:
                                dseecundaria += 1
                            if self.matriz[i+c][j-c] == Tabuleiro.JOGADOR_X:
                                dseecundaria += 4

                if linha == 1:
                    if coluna == 1 or dprincipal == 1 or dseecundaria == 1:
                        return (i, j)
                elif coluna == 1:
                    if dprincipal == 1 or dseecundaria == 1:
                        return(i, j)
                ''' o único quadrado que pertence a ambas diagonais será marcado no requisito seguinte(verficação desnecessária)
                elif dprincipal == 1 and dseecundaria == 1:
                    return(i, j)'''
             
        # r3: Se o quadrado central estiver livre, marque-o.
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        #r4: Se seu oponente tiver marcado um dos cantos, marque o canto oposto.
        if self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return(2,2)
        if self.matriz[0][2] == Tabuleiro.JOGADOR_X and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return(2,0)
        if self.matriz[2][0] == Tabuleiro.JOGADOR_X and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return(0,2)
        if self.matriz[2][2] == Tabuleiro.JOGADOR_X and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return(0,0)

        # r5: Se houver um canto vazio, marque-o.
        cantos = []
        if self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            cantos.append((0, 0))
        if self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            cantos.append((0, 2))
        if self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            cantos.append((2, 0))
        if self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            cantos.append((2, 2))

        if len(cantos) > 0:
            return choice(cantos)

        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                    
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        
