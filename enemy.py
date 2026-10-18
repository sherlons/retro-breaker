import pygame, random
from config import LANES_Y
import os

class Enemy:
    def __init__(self, x, difficulty_level):
        self.lane = random.choice([0,1,2,3,4])
        self.x = x
        self.y = LANES_Y[self.lane]
        self.width = 80
        self.height = 70
        base_speed = 1.5 + difficulty_level * 0.15
        self.speed = random.uniform(base_speed, base_speed+1.0)
        self.drop_chance = 0.18

        # sprite
        self.sprite = None
        path = "assets/enemy.png"
        if os.path.exists(path):
            try:
                img = pygame.image.load(path).convert_alpha()
                self.sprite = pygame.transform.scale(img, (self.width, self.height))
            except: pass

    def update(self): 
        self.x -= self.speed

    def draw(self, screen, camera_x):
        if self.sprite:
            screen.blit(self.sprite, (self.x - camera_x, self.y - 10))
        else:
            pygame.draw.rect(screen, (255,50,50), (self.x - camera_x, self.y, self.width, self.height))