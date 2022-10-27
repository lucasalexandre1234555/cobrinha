import pygame
import time
import random

pygame.init()

largura = 500
altura = 300

dis = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo da cobrinha')

clock = pygame.time.Clock()

bloco = 10
velocidade = 15

estilo_fonte = pygame.font.SysFont("", 25) #25  #bahnschrift
pontos_fonte = pygame.font.SysFont("", 25) #35  #comicsansms

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)


def pontos(score):
    value = pontos_fonte.render("pontos: " + str(score), True, branco)
    dis.blit(value, [0, 0])


def cobrinha(bloco, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, branco, [x[0], x[1], bloco, bloco])


def mensagem1(msg, color):
    mesg = estilo_fonte.render(msg, True, color)
    dis.blit(mesg, [largura / 8, altura / 4])
    
def mensagem2(msg, color):
    mesg = estilo_fonte.render(msg, True, color)
    dis.blit(mesg, [largura / 8, altura / 3])
    
    


def gameLoop():
    game_over = False
    fim_do_jogo = False

    x1 = largura / 2
    y1 = altura / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, largura - bloco) / 10.0) * 10.0
    foody = round(random.randrange(0, altura - bloco) / 10.0) * 10.0

    while not game_over:

        while fim_do_jogo == True:
            dis.fill(preto)
            mensagem1("você perdeu! Aperte P para jogar novamente", branco)
            mensagem2("aperte Q para fechar o jogo", branco)
            pontos(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        fim_do_jogo = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -bloco
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = bloco
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -bloco
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = bloco
                    x1_change = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_do_jogo = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(preto)
        pygame.draw.rect(dis, verde, [foodx, foody, bloco, bloco])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                fim_do_jogo = True

        cobrinha(bloco, snake_List)
        pontos(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, largura - bloco) / 10.0) * 10.0
            foody = round(random.randrange(0, altura - bloco) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()


gameLoop()
