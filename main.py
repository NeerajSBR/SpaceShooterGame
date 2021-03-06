import pygame
from pygame.constants import K_RIGHT

pygame.init()

screen = pygame.display.set_mode((800,600))


# title

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player 

playerImg = pygame.image.load('bleh.png')
playerX = 370
playerY = 480

# variable for movement 

playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

# game loop
running = True
while running:

    screen.fill((0,0,0))    
    
     
    # loop for event
    for event in pygame.event.get():

        
        
        if event.type == pygame.QUIT:
            running = False

        # key stroke

        if event.type == pygame.KEYDOWN:
            print("Key pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:    
                playerX_change = 0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerX_change = 0
                playerY_change = 0
                

    # it will move  
    playerX += playerX_change
    playerY += playerY_change
    player(playerX,playerY)
    pygame.display.update()
