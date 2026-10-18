import pygame
import random
from player import Player
from enemy import Enemy

# inicio
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Breaker - Runner")
clock = pygame.time.Clock()

# jugador
player = Player(100, 500)

# ESTO TE FALTABA - enemigos infinitos
enemies = []
enemy_timer = 0
W = SCREEN_WIDTH

# Corazon del juego
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movimiento
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.shoot(keys)
    player.update()

    # Generar enemigos infinitos
    enemy_timer += 1
    if enemy_timer > 90: # cada 1.5 segundos
        enemies.append(Enemy(player.x + W + random.randint(0, 200), 500))
        enemy_timer = 0

    for e in enemies[:]:
        e.update()
        # Colision bala -> enemigo
        for b in player.bullets[:]:
            if (b.x < e.x + e.width and b.x + b.width > e.x and 
                b.y < e.y + e.height and b.y + b.height > e.y):
                if e in enemies:
                    enemies.remove(e)
                if b in player.bullets:
                    player.bullets.remove(b)
                break
        # Colision enemigo -> jugador
        if e.x < player.x + player.width and e.x + e.width > player.x and e.y < player.y + player.height and e.y + e.height > player.y:
            if e in enemies:
                enemies.remove(e)
            player.lives -= 1
            if player.lives <= 0: 
                running = False
        if e.x < player.x - 500:
            if e in enemies:
                enemies.remove(e)

    # CAMARA FIJA AL JUGADOR
    camera_x = player.x - 150
    
    # dibujo
    screen.fill((30, 30, 80))

    # Piso infinito
    for i in range(-1, 5):
        x_piso = (i * 800) - (camera_x % 800)
        pygame.draw.rect(screen, (100,100,100), (x_piso, 550, 800, 50))

    player.draw(screen, camera_x)
    for e in enemies:
        e.draw(screen, camera_x)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
print("Game Over!")