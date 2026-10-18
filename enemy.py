import pygame, random
from config import LANES_Y

class Enemy:
    def __init__(self, x, difficulty_level):
        self.lane = random.choice([0,1,2,3,4])
        self.x = x
        self.y = LANES_Y[self.lane]
        self.width = 50
        self.height = 50
        base_speed = 1.5 + difficulty_level * 0.15 # mucho mas lento el aumento
        self.speed = random.uniform(base_speed, base_speed+1.0)
        self.drop_chance = 0.18 # antes 0.4, ahora solo 18% deja caja

    def update(self): 
        self.x -= self.speed

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, (255,50,50), (self.x - camera_x, self.y, self.width, self.height))