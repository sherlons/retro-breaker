import pygame, random
from player import Player
from enemy import Enemy
from pickup import Pickup
from config import LANES_Y, MAX_PLAYER_SPEED, SPEED_INCREASE_PER_SEC, START_PLAYER_SPEED

pygame.init()
W,H=800,600
screen=pygame.display.set_mode((W,H))
clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 32)
bigfont=pygame.font.SysFont(None, 64)

def game_loop():
    player=Player()
    enemies=[]; pickups=[]
    timer_spawn=0
    score=0
    time_played=0
    difficulty=0
    running=True

    while running:
        dt = clock.tick(60) / 1000.0
        time_played += dt
        difficulty = time_played * 0.1 # sube 10x mas lento que antes

        if player.run_speed < MAX_PLAYER_SPEED:
            player.run_speed += SPEED_INCREASE_PER_SEC * dt * 60

        for e in pygame.event.get():
            if e.type==pygame.QUIT: 
                return -1, 0 # -1 = salir del juego total

        keys=pygame.key.get_pressed()
        player.move(keys); player.shoot(keys); player.update()

        timer_spawn+=1
        spawn_rate = max(35, 120 - int(difficulty * 4)) # empieza cada 2 segundos, baja a 0.5 seg
        if timer_spawn > spawn_rate:
            enemies.append(Enemy(player.x+W+random.randint(0,300), difficulty))
            timer_spawn=0

        for en in enemies[:]:
            en.update()
            for b in player.bullets[:]:
                if b.lane==en.lane and b.x < en.x+en.width and b.x+b.width > en.x:
                    if random.random() < en.drop_chance:
                        tipo = random.choice(["ammo","life"])
                        pickups.append(Pickup(en.x, en.lane, tipo))
                    enemies.remove(en); player.bullets.remove(b)
                    score+=100
                    break
            if en.lane==player.lane and en.x < player.x+player.width and en.x+en.width > player.x:
                enemies.remove(en); player.lives-=1
                if player.lives<=0: 
                    return score, time_played
            if en.x < player.x-600: enemies.remove(en)

        for p in pickups[:]:
            if p.lane==player.lane and p.x < player.x+player.width and p.x+p.width > player.x:
                if p.tipo=="ammo" and player.max_bullets_on_screen < 3:
                    player.max_bullets_on_screen+=1
                if p.tipo=="life" and player.lives < player.max_lives:
                    player.lives+=1
                score+=50
                pickups.remove(p)

        score += int(player.run_speed / 3)

        camera_x = player.x - 150
        screen.fill((20,10,50))
        for i, y in enumerate(LANES_Y):
            color = (60,60,60) if i!=player.lane else (90,90,100)
            pygame.draw.rect(screen, color, (0, y, 2000, 60))

        player.draw(screen, camera_x)
        for en in enemies: en.draw(screen, camera_x)
        for p in pickups: p.draw(screen, camera_x)

        # HUD FIX: ahora no se enciman los numeros
        pygame.draw.rect(screen, (0,0,0), (0,0,W,55))
        screen.blit(font.render(f"VIDAS: {player.lives}/{player.max_lives}", True, (255,255,255)), (10,5))
        screen.blit(font.render(f"BALAS MAX: {player.max_bullets_on_screen}", True, (255,255,0)), (200,5))
        screen.blit(font.render(f"PTS: {score}", True, (255,255,255)), (400,5))
        screen.blit(font.render(f"VEL: {player.run_speed:.1f}", True, (0,255,255)), (600,5))

        pygame.display.flip()

    return score, time_played

# LOOP PRINCIPAL CON MENU
estado = "playing"
while True:
    score, t = game_loop()
    if score == -1: break # cerro ventana

    # Pantalla GAME OVER
    waiting=True
    while waiting:
        screen.fill((20,10,50))
        screen.blit(bigfont.render("PERDISTE", True, (255,50,50)), (W//2-120, H//2-100))
        screen.blit(font.render(f"Puntaje final: {score}", True, (255,255,255)), (W//2-100, H//2-20))
        screen.blit(font.render(f"Tiempo: {t:.1f}s", True, (255,255,255)), (W//2-70, H//2+10))
        screen.blit(font.render("Presiona R para volver a empezar", True, (255,255,0)), (W//2-180, H//2+60))
        screen.blit(font.render("ESC para salir", True, (200,200,200)), (W//2-80, H//2+90))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: waiting=False; estado="exit"
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_r: waiting=False
                if e.key==pygame.K_ESCAPE: waiting=False; estado="exit"
        clock.tick(60)
    if estado=="exit": break

pygame.quit()