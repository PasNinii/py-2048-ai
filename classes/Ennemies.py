class Ennemies:
    def __init__(self, ennemies):
        self.ennemies = ennemies

    def move(self, screen):
        for ennemy in self.ennemies:
            if (ennemy.position_y > 600):
                self.ennemies.remove(ennemy)
            ennemy.move(screen)