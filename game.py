#bibliotecas
import pygame
import win32com.client as win32
import numpy

#------------------------------------------------------

#cores e formas
preto = (0,0,0)
branco = (255,255,255)
azul_claro = (172.89,215.985,230.01)
marrom = (128,0,0)
verde = (0,255,0)

PI = 3,14


#------------------------------------------------------

#janela do jogo
pygame.init()

janela = pygame.display.set_mode((400,600))
pygame.display.set_caption("flappy birdy")

janela.fill(azul_claro)

#desenhos e fontes
fonte = pygame.font.Font("fonte\FlappyBirdy.ttf", 75)
texto = fonte.render("flappy birdy",True,preto)
janela.blit(texto,[90,25])

pygame.draw.line(janela,marrom,(0,545),(400,545),4)
pygame.draw.rect(janela,verde,(0,548,400,550))


pygame.display.update()

deve_continuar  = True

#loop do jogo
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False 
            


pygame.quit()

#-----------------------------------------------------




























