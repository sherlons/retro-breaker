import pygame
class Pickup:
    def __init__(self, x, lane, tipo="ammo"):
        from config import LANES_Y
        self.x = x; self.y = LANES_Y[lane]
        self.lane = lane; self.tipo = tipo # ammo o life
        self.width = 30; self.height = 30
    def draw(self, screen, camera_x):
        color = (0,255,255) if self.tipo=="ammo" else (0,255,0)
        pygame.draw.rect(screen, color, (self.x - camera_x, self.y+10, self.width, self.height))