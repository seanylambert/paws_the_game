import pygame

class Character():
    def __init__(self, x, y, width, height, color = 'red'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_direction = 0
        self.y_direction = 0
        self.walk_speed = 0.1
        self.color = color
    def move(self):                     #0,0 *right x-increase *down y-increase
        self.x += (self.x_direction * self.walk_speed)
        self.y += (self.y_direction * self.walk_speed)
        w, h = pygame.display.get_surface().get_size()
        if self.x < 0:
            self.x = 0
        elif self.x > w - self.width:
            self.x = w - self.width

        if self.y < 0:
            self.y = 0
        elif self.y > h - self.height:
            self.y = h - self.height

        if (self.x_direction != 0):
            print("x:", self.x, self.x_direction)
        if (self.y_direction != 0):
            print("y:", self.y, self.y_direction)
    def update(self):
        self.move()
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))              #(x,y, width, height) == tuple

