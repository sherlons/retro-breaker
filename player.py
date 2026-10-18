import pygame
from bullet import Bullet
from config import LANES_Y, START_PLAYER_SPEED

class Player:
    def __init__(self):
        self.lane = 2
        self.x = 100
        self.y = LANES_Y[self.lane]
        self.target_y = self.y
        self.width = 50
        self.height = 60
        self.speed = 18
        self.run_speed = START_PLAYER_SPEED
        self.lives = 3 # te doy 3 de inicio para que no mueras tan rapido
        self.max_lives = 3
        self.max_bullets_on_screen = 1
        self.bullets = []
        self.shoot_cooldown = 0
        self.lane_cooldown = 0 # nuevo, para que no se cambie loco

    def move(self, keys):
        if self.lane_cooldown > 0:
            self.lane_cooldown -= 1
            return
        if keys[pygame.K_w] and self.lane > 0:
            self.lane -= 1
            self.target_y = LANES_Y[self.lane]
            self.lane_cooldown = 12 # espera un poquito
        if keys[pygame.K_s] and self.lane < 4:
            self.lane += 1
            self.target_y = LANES_Y[self.lane]
            self.lane_cooldown = 12
        
        if self.y < self.target_y: self.y += self.speed
        if self.y > self.target_y: self.y -= self.speed
        if abs(self.y - self.target_y) < self.speed: self.y = self.target_y

    def shoot(self, keys):
        if self.shoot_cooldown > 0: self.shoot_cooldown -= 1
        if keys[pygame.K_f] and self.shoot_cooldown==0 and len(self.bullets) < self.max_bullets_on_screen:
            self.bullets.append(Bullet(self.x+self.width, self.y+25, self.lane))
            self.shoot_cooldown = 20 # un poco mas lento para no spamear

    def update(self):
        self.x += self.run_speed
        for b in self.bullets[:]:
            b.update()
            if b.x > self.x + 900: self.bullets.remove(b)

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, (0,255,180), (self.x-camera_x, self.y, self.width, self.height))
        for b in self.bullets: b.draw(screen, camera_x)