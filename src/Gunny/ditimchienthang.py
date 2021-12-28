import pygame
from HealthBar import HealthBar   
from Settings import Settings
import GameFunction as gf
from Characters import Character
def run_game():

    pygame.init()
    g_settings = Settings()
    character_a = Character('assets/nv1.png')
    character_b = Character('assets/player1.png')
    healthBar_a = HealthBar('assets/redHealthBar.png')
    healthBar_b = HealthBar('assets/blueHealthBar.png')
    bulletpicture = pygame.transform.smoothscale(pygame.image.load('assets/bullet.png'),(100,50))
    clock = pygame.time.Clock()
    clock.tick(g_settings.FPS)
    window = pygame.display.set_mode(
        (g_settings.window_width, g_settings.window_height)
    )
    pygame.display.set_caption("Gunny")
    
    bullets = []
    click = 0

    while True:
        
        gf.check_events(bullets, click)
        gf.update_screen(g_settings, window)

        for b in range(len(bullets)):

                bullets[b][0] += 5

        for bullet in bullets[:]:
            if bullet[0] < 0:
                bullets.remove(bullet)
    
        window.blit(g_settings.bg,(0,0))
        

        for bullet in bullets:
            
                window.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
            

        

        window.blit(character_a.image,(0,390))
        window.blit(character_b.image,(g_settings.window_width-120,390))
        window.blit(healthBar_a.image,(0,0))
        window.blit(pygame.transform.flip(healthBar_b.image,True,False),(g_settings.window_width-400,0))


run_game()
