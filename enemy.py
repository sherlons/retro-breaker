import pygame
import random
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (255, 50, 50)
        self.speed = random.randint(3, 6)
        self.alive = True
    def update(self):
        self.x -= self.speed
    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y, self.width, self.height))