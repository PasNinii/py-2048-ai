################################
# * General Modules
import pygame
import random
# * Utils Modules
from classes.Player import Player
from classes.Ennemy import Ennemy
from classes.Ennemies import Ennemies
from resources.settings.settings import Settings
################################
################################
def init_screen(screen, background):
    # * Title and Icon
    pygame.display.set_caption(Settings.NAME)
    icon = pygame.image.load(Settings.PATH + "game_logo.png")
    background = pygame.image.load(Settings.PATH + background)
    background = pygame.transform.scale(background, Settings.SIZE)
    pygame.display.set_icon(icon)
    screen.fill(Settings.COLO)
    screen.blit(background, (0,0))

def init_characters():
    player = Player(position_x=370,
                    position_y=480,
                    icon=Settings.PATH + "player_icon.png")
    list_ennemies = [
        Ennemy(icon=Settings.PATH + "ennemy_cake.png",
                    change_position_x=2,
                    change_position_y=0.01),
        Ennemy(icon=Settings.PATH + "ennemy_dessert.png",
                    change_position_x=4,
                    change_position_y=0.01),
        Ennemy(icon=Settings.PATH + "ennemy_hotdog.png",
                    change_position_x=6,
                    change_position_y=0.01),
        Ennemy(icon=Settings.PATH + "ennemy_popcorn.png",
                    change_position_x=8,
                    change_position_y=0.01)
    ]
    ennemies = Ennemies(list_ennemies)
    return player, ennemies