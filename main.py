################################
# * Import modules
import pygame
import random
import sys
# * Utils Modules
from resources.settings import Settings
from utils.move import move, boundaries
from utils.init import init
################################
################################
# * Initialize the pygame
pygame.init()
# * Create the screen, with resolution param
screen = pygame.display.set_mode(Settings.SIZE)



while (True):
    init(screen)
    for event in pygame.event.get():
        # * if keystroke is pressed check wheher it's right or lef
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                playerX_change = -0.3
            elif (event.key == pygame.K_RIGHT):
                playerX_change = 0.3
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0
        # ! To end the game :'(
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(2)


    # * RGB color
    playerX += playerX_change
    ennemyX += ennemyX_change
    playerX = boundaries(playerX)
    ennemyX = boundaries(ennemyX)
    move(player_icon, playerX, playerY)
    move(ennemy_icon, ennemyX, ennemyY)
    pygame.display.update()