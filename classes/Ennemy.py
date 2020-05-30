
from classes.Character import Character

class Ennemy(Character):
    def __init__(self, position_x=0, position_y=0, icon='', change_position_x=0, change_position_y=0):
        super().__init__(position_x=position_x, position_y=position_y, icon=icon, change_position_x=change_position_x, change_position_y=change_position_y)

    def move(self, screen):
        self.position_x += self.change_position_x
        self.position_y += self.change_position_y
        super().move(screen)

    def check_boundaries(self):
        if (self.position_x > 736.0):
            self.change_position_x = -self.change_position_x
            self.change_position_y *= 2
        elif (self.position_x < 0.0):
            self.change_position_x = -self.change_position_x
            self.change_position_y *= 2