################################
# TODO: add mother class if needed like weapon
# TODO: maybe create class obj more general, because all object might have coordinate
# * General Modules
import pygame
# * Utils Modules
from resources.settings.settings import Settings
################################
################################
class Bullet:
    # ! Exact same constructor as character
    def __init__(self, position_x: float = 0,
                 position_y: float = 0,
                 icon: str = "",
                 change_position_x: float = 0,
                 change_position_y: float = 0,
                 bullet_state: bool = True):
        self.position_x = position_x
        self.position_y = position_y
        self.change_position_x = change_position_x
        self.change_position_y = change_position_y
        self.icon = pygame.image.load(icon)
        self.bullet_state = bullet_state

    def check_boundaries(self):
        if (self.position_y <= 0):
            self.position_y = 480
            self.bullet_state = True

    def move(self, screen, player_position_x: float):
        self.bullet_state = False
        self.position_x = player_position_x
        self.position_y -= self.change_position_y
        screen.blit(self.icon,
                    (self.position_x + 16, self.position_y + 10))