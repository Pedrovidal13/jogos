import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
tela_altura = 600
tela_largura = 600

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Jogo da cobrinha")

pygame.mixer.music.set_volume(0.1)
musica = pygame.mixer.music.load("BoxCat Games - Against the Wall.mp3")
tocar_musica = pygame.mixer.music.play(-1)
musica_colisao = pygame.mixer.Sound("smw_dragon_coin.wav")

largura_personagem = 20
altura_personagem = 20
velocidade = 5

x_cobra = int(tela_altura / 2 - altura_personagem / 2)
y_cobra = int(tela_largura / 2 - largura_personagem / 2)

x_controle = 5
y_controle = 0

x_maca = randint(10, 550)
y_maca = randint(10, 550)

fonte = pygame.font.SysFont("arialblack", 30, True, True)

frames = pygame.time.Clock()
pontos = 0

comprimento_cobra = 5
lista_corpo = []

morreu = False


def aumenta_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela, (255, 50, 50), (XeY[0], XeY[1], altura_personagem, largura_personagem))


def reiniciar_game():
    global pontos, comprimento_cobra, x_cobra, y_cobra, x_maca, y_maca, morreu, lista_cabeca, lista_corpo
    pontos = 0
    comprimento_cobra = 5
    x_cobra = int(tela_altura / 2 - altura_personagem / 2)
    y_cobra = int(tela_largura / 2 - largura_personagem / 2)
    lista_corpo = []
    lista_cabeca = []
    x_maca = randint(10, 550)
    y_maca = randint(10, 550)
    morreu = False


run = True
while run:

    frames.tick(30)
    pygame.time.delay(5)
    mensagem = f"Pontos:  {pontos}"
    texto_formatado = fonte.render(mensagem, False, (55, 250, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_a]:
            x_controle -= velocidade
            y_controle = 0
            if x_controle == velocidade:
                pass

            else:
                x_controle = -velocidade
                y_controle = 0

        if tecla[pygame.K_d]:
            if x_controle == -velocidade:
                pass

            else:
                x_controle = velocidade
                y_controle = 0

        if tecla[pygame.K_w]:
            if y_controle == velocidade:
                pass

            else:
                y_controle = -velocidade
                x_controle = 0
        if tecla[pygame.K_s]:
            if y_controle == -velocidade:
                pass

            else:
                y_controle = velocidade
                x_controle = 0

        if tecla[pygame.K_LEFT]:
            x_controle -= velocidade
            y_controle = 0
            if x_controle == velocidade:
                pass

            else:
                x_controle = -velocidade
                y_controle = 0

        if tecla[pygame.K_RIGHT]:
            if x_controle == -velocidade:
                pass

            else:
                x_controle = velocidade
                y_controle = 0

        if tecla[pygame.K_UP]:
            if y_controle == velocidade:
                pass

            else:
                y_controle = -velocidade
                x_controle = 0
        if tecla[pygame.K_DOWN]:
            if y_controle == -velocidade:
                pass

            else:
                y_controle = velocidade
                x_controle = 0


    x_cobra += x_controle
    y_cobra += y_controle
    tela.fill((0, 0, 0))

    cobra = pygame.draw.rect(tela, (255, 50, 50), (x_cobra, y_cobra, largura_personagem, altura_personagem))
    maca = pygame.draw.circle(tela, (25, 150, 200), (x_maca, y_maca), 10)

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 550)
        pontos += 1
        musica_colisao.play()
        comprimento_cobra += 2
        velocidade += 0.25

    lista_cabeca = []

    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_corpo.append(lista_cabeca)

    if lista_corpo.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont("arialblack", 30, True)
        mensagem_morte1 = f"GAME OVER!"
        mensagem_morte2 = f"Press 'R' for reset game"
        texto_formatado2 = fonte.render(mensagem_morte1, True, (55, 250, 0))
        texto_formatado3 = fonte.render(mensagem_morte2, True, (55, 250, 0))
        morreu = True
        while morreu:
            tela.fill((0, 0, 0))



            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_game()
            tela.blit(texto_formatado2, (230, 250))
            tela.blit(texto_formatado3, (155, 275))
            pygame.mixer.music.pause()
            pygame.display.update()

    if x_cobra > tela_largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = tela_largura
    if y_cobra > tela_altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = tela_altura

    if len(lista_corpo) > comprimento_cobra:
        del lista_corpo[0]


    aumenta_cobra(lista_corpo)

    tela.blit(texto_formatado, (420, 30))
    pygame.mixer.music.unpause()
    pygame.display.update()
pygame.quit()

""" circulo pygame.draw.circle(tela, (125, 150,  200), (250, 250), 30)
    linha pygame.draw.line(tela, (10, 100, 0), (250, 0), (250, 350),5)"""
