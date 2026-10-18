import pygame
from bullet import Bullet
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 60
        self.color = (0, 255, 180)
        self.vel_y = 0
        self.jump_power = -20
        self.gravity = 1
        self.on_ground = False
        self.bullets = []
        self.shoot_cooldown = 0
        self.lives = 3
        self.auto_speed = 4 # velocidad que corre solo hacia el frente

    def move(self, keys):
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def shoot(self, keys):
        if self.shoot_cooldown > 0: self.shoot_cooldown -= 1
        if keys[pygame.K_f] and self.shoot_cooldown == 0:
            self.bullets.append(Bullet(self.x + self.width, self.y + 20))
            self.shoot_cooldown = 15

    def update(self):
        self.x += self.auto_speed # CORRE SOLO
        self.vel_y += self.gravity
        self.y += self.vel_y
        if self.y + self.height >= 550:
            self.y = 550 - self.height
            self.vel_y = 0
            self.on_ground = True
        for b in self.bullets[:]:
            b.update()
            if b.x > self.x + 900:
                self.bullets.remove(b)

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y, self.width, self.height))
        for b in self.bullets:
            b.draw(screen, camera_x)

    def move(self, keys):
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def shoot(self, keys):
        if self.shoot_cooldown > 0: self.shoot_cooldown -= 1
        if keys[pygame.K_f] and self.shoot_cooldown == 0:
            self.bullets.append(Bullet(self.x + self.width, self.y + 20))
            self.shoot_cooldown = 15

    def update(self):
        self.x += self.auto_speed # CORRE SOLO
        self.vel_y += self.gravity
        self.y += self.vel_y
        if self.y + self.height >= 550:
            self.y = 550 - self.height
            self.vel_y = 0
            self.on_ground = True
        for b in self.bullets[:]:
            b.update()
            if b.x > self.x + 900:
                self.bullets.remove(b)

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y, self.width, self.height))
        for b in self.bullets:
            b.draw(screen, camera_x)