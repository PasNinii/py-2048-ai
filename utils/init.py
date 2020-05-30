################################
# * General Modules
import pygame
import random
# * Utils Modules
from resources.settings import Settings
################################
################################
def init(screen):
    # * Title and Icon
    pygame.display.set_caption(Settings.NAME)
    icon = pygame.image.load(Settings.PATH + "game_logo.png")
    background = pygame.image.load(Settings.PATH + "background.png")
    background = pygame.transform.scale(background, Settings.SIZE)
    pygame.display.set_icon(icon)
    # * Player
    player_icon = pygame.image.load(Settings.PATH + "player_icon.png")
    playerX = 370.0
    playerY = 480.0
    playerX_change = 0
    playerX_change = 0
    # * Ennemy
    ennemy_icon = pygame.image.load(Settings.PATH + "ennemy_icon.png")
    ennemyX = random.randint(0, 800)
    ennemyY = random.randint(50, 150)
    ennemyX_change = 0.5
    ennemyY_change = 0
    screen.fill((192, 192, 192))
    screen.blit(background, (0,0))
    