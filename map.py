import pygame

class Map():
    def __init__(self, x, y, width, height, color = 'red'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_direction = 0
        self.y_direction = 0
        self.color = color
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height)) 