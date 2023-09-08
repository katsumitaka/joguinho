import pygame
from pygame import *
import random

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def colision(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) 


up = 0
right = 1
down = 2
left = 3



pygame.init()

#tela
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('snake')

#cobra
snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((5, 77, 7))

my_direction = left

#fps
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

#maça
apple_position = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

game_over = False

while not game_over:
    clock.tick(20)
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        #movimento
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = up
            if event.key == K_DOWN:
                my_direction = down
            if event.key == K_LEFT:
                my_direction = left
            if event.key == K_RIGHT:
                my_direction = right

    #colisão com a maça
    if colision(snake[0],apple_position):
        apple_position = on_grid_random()
        snake.append((0,0))
        score += 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake [0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break


    #colisão da cobra com ela msm
    for i in range(1, len(snake) -1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
    
    if game_over:
        break


    #movimento da cobra
    for i in range (len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == up:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == left:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == right:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == down:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    #cor da maça
    screen.fill((52, 235, 58))
    screen.blit(apple,apple_position)

   
    
    score_font = font.render('Score: %s' % (score), True, (255,255,255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)


    for pos in snake:
        screen.blit(snake_skin,pos)
    pygame.display.update()
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf',75)
    game_over_screen = game_over_font.render('Game Over', True, (255,255,255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2 , 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()