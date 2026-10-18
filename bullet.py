import pygame

class Bullet:
    def __init__(self, x, y, direction=1):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 5
        self.speed = 10 * direction
        self.color = (255, 255, 0)

    def update(self):
        self.x += self.speed

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y, self.width, self.height))