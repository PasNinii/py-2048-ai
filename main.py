################################
# * Import modules
import pygame
import random
import sys
# * Utils Modules
from resources.settings.settings import Settings
from utils.init import init_screen, init_characters
################################
################################
# * Initialize the pygame
pygame.init()
# * Create the screen, with resolution param
screen = pygame.display.set_mode(Settings.SIZE)
player, ennemies = init_characters()
COUNTER = 0
background = "background.png"
while (True):
    init_screen(screen, background)
    for event in pygame.event.get():
        # * if keystroke is pressed check wheher it's right or lef
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                player.change_rate(-0.8)
            elif (event.key == pygame.K_RIGHT):
                player.change_rate(0.8)
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player.change_rate()
        # ! To end the game :'(
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(2)
    for ennemy in ennemies:
        ennemy.move(screen)
    player.move(screen)
    # ! update every iteration
    COUNTER += 1
    if (COUNTER > 200):
        background = "background_2.png"
    if (COUNTER > 400):
        background = "background_3.jpg"
    if (COUNTER > 600):
        background = "background_4.gif"
    pygame.display.update()


"""
while (True):
    for event in pygame.event.get():
        # * if keystroke is pressed check wheher it's right or lef
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                player.change_rate(-0.3)
            elif (event.key == pygame.K_RIGHT):
                player.change_rate(0.3)
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player.change_rate(0)
        # ! To end the game :'(
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(2)

    player.move()
    player.check_boundaries()
    move(screen, player)
    # * RGB color
    playerX += playerX_change
    ennemyX += ennemyX_change
    playerX = boundaries(playerX)
    ennemyX = boundaries(ennemyX)
    move(player_icon, playerX, playerY)
    move(ennemy_icon, ennemyX, ennemyY)
    pygame.display.update()"""