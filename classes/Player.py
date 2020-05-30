from classes.Character import Character

class Player(Character):
    def __init__(self,
                 position_x: float = 0.0,
                 position_y: float = 0.0,
                 icon: str = "",
                 change_position_x: float = 0.0,
                 change_position_y: float = 0.0):
        super().__init__(position_x, position_y, icon, change_position_x, change_position_y)


    def move(self, screen):
        self.position_x += self.change_position_x
        super().move(screen)

    def check_boundaries(self):
        if (self.position_x > 800.0):
            self.position_x = 0.0
        elif (self.position_x < 0.0):
            self.position_x = 800.0