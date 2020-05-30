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
background = "background.png"
while (True):
    init_screen(screen, background)
    for event in pygame.event.get():
        # * if keystroke is pressed check wheher it's right or lef
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                player.change_rate(-5)
            elif (event.key == pygame.K_RIGHT):
                player.change_rate(5)
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player.change_rate()
        # ! To end the game :'(
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(2)
    ennemies.move(screen)
    player.move(screen)
    # ! update every iteration
    pygame.display.update()