import pygame
from player import Player

# inicio
pygame.init()
SCREEN_WIDTH = 800
SCREEN_NEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_NEIGHT))
pygame.display.set_caption("Retro Breaker")
clock = pygame.time.Clock()

# jugador
player =Player(375, 500)

# Corazon del juego
running = True
while running: 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

    # movimiento
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.shoot(keys)
    player.update()

 # CAMARA: el jugador siempre al medio
    camera_x = player.x - SCREEN_WIDTH // 2 + player.width // 2
    
    # dibujo
    screen.fill((30, 30, 80)) # fondo morado 

    # Piso infinito - dibujamos 3 pantallas de piso
    for i in range(-1, 5):
        x_piso = (i * 800) - (camera_x % 800)
        pygame.draw.rect(screen, (100,100,100), (x_piso, 550, 800, 50))


    player.draw(screen, camera_x)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
