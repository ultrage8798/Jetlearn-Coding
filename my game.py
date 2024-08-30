import pygame
from time import *
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((600,600))

player=pygame.image.load("rocket.png")
bg=pygame.image.load("roadbg.png")

player_rect=player.get_rect()
player_x,player_y=player_rect.topleft

keys=[False, False, False, False]
running=True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEFT:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[1]=False
            elif event.key==K_LEFT:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False

    if keys[0]:
        if player_y>0:
            player_y-=7
    elif keys[1]:
        if player_y<536:
            player_y+=7
    elif keys[2]:
        if player_x>0:
             player_x-=7
    elif keys[3]:
        if player_x<536:
            player_x+=7
    
    player_rect.topleft=(player_x,player_y)

    screen.fill((0,0,0))

    screen.blit(bg,(0,0))
    screen.blit(player,player_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
print("Game Over")