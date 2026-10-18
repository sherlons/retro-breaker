import pygame
class Bullet:
    def __init__(self, x, y, lane):
        self.x = x; self.y = y; self.lane = lane
        self.width = 20; self.height = 8
        self.speed = 12
    def update(self): self.x += self.speed
    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, (255,255,0), (self.x - camera_x, self.y - 10, self.width, self.height))