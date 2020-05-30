import abc
import pygame

class Character(metaclass=abc.ABCMeta):
    def __init__(self, position_x: float = 0,
                 position_y: float = 0,
                 icon: str = "",
                 change_position_x: float = 0,
                 change_position_y: float = 0):
        """Constructor of character class

        Keyword Arguments:
            position_x {float} -- Starting position on x-axis (default: {0})
            position_y {float} -- Starting position on y-axis (default: {0})
            icon {str} -- Name of images, has to be saved in resources/images/ folder (default: {""})
            change_position_x {float} -- default change position rate on x-axis (default: {0})
            change_position_y {float} -- default change poistion rate on y-axis (default: {0})
        """
        self.position_x = position_x
        self.position_y = position_y
        self.icon = pygame.image.load(icon)
        self.change_position_x = change_position_x
        self.change_position_y = change_position_y

    def move(self, screen):
        """Change coordinate accordingly to the value

        Keyword Arguments:
            change_position_x {int} -- distance on x-axis (default: {0})
            change_position_y {int} -- distance on y-axis (default: {0})
        """
        self.check_boundaries()
        screen.blit(self.icon, (self.position_x, self.position_y))

    @abc.abstractmethod
    def check_boundaries(self):
        """Check if element goes out of screen
        """
        pass

    def change_rate(self, change_position_x: float = 0.0, change_position_y: float = 0.0):
        """Change the default rate

        Keyword Arguments:
            change_position_x {float} -- increase or decrease default rate (default: {0})
            change_position_y {float} -- increase or decrease default rate (default: {0})
        """
        self.change_position_x = change_position_x
        self.change_position_y = change_position_y
