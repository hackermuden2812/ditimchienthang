import pygame
from pygame.constants import K_SPACE, MOUSEBUTTONUP
from HealthBar import HealthBar
from Settings import Settings
import GameFunction as gf
from Characters import Character
import time

def run_game():

    pygame.init()
    g_settings = Settings()
    character_a = Character('src/Gunny/assets/nv1.png', 1)
    character_b = Character('src/Gunny/assets/player1.png', -1)
    healthBar_a = HealthBar('src/Gunny/assets/redHealthBar.png')
    healthBar_b = HealthBar('src/Gunny/assets/blueHealthBar.png')
    bulletpicture = pygame.transform.smoothscale(
        pygame.image.load('src/Gunny/assets/bullet.png'), (100, 50))
    clock = pygame.time.Clock()
    clock.tick(g_settings.FPS)
    window = pygame.display.set_mode(
        (g_settings.window_width, g_settings.window_height)
    )
    pygame.display.set_caption("Gunny")

    bulletsA = []
    bulletsB = []
    bullets=[]
    count =0
    

    while True:
        
        gf.update_screen(g_settings, window)
        if character_a.turn:
            gf.check_events(bulletsA, 0)
            for b in range(len(bulletsA)):
                if  bulletsA[b][0] < g_settings.window_width:
                    bulletsA[b][0] += 5*character_a.direction

            for bullet in bulletsA[:]:
                if bullet[0] > g_settings.window_width:
                    bulletsA.remove(bullet)
        
            window.blit(g_settings.bg,(0,0))          

            for bullet in bulletsA:                
                    window.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

            print("Bullets A")
            print(bulletsA)     
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:  
                    fire()    
                    character_a.turn = False
                    character_b.turn = True

            # time.sleep(1)
        elif character_b.turn:
            gf.check_events(bulletsB, 1)

            for b in range(len(bulletsB)):
                if bulletsB[b][0] >0:
                    bulletsB[b][0] += 5*character_b.direction
            for bullet in bulletsB[:]:
                if bullet[0] < 0:
                    bulletsB.remove(bullet)
        
            window.blit(g_settings.bg,(0,0))
            for bullet in bulletsB:                
                    window.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
            print("Bullets B" )
            print(bulletsB)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:    
                    fire()                
                    character_b.turn = False
                    character_a.turn = True

            # time.sleep(1)
        window.blit(character_a.image,(0,390))
        window.blit(character_b.image,(g_settings.window_width-120,390))
        window.blit(healthBar_a.image,(0,0))
        window.blit(pygame.transform.flip(healthBar_b.image,True,False),(g_settings.window_width-400,0))
        def fire ():
            pygame.mixer.init()
            pygame.mixer.music.load('src/Gunny/assets/fireSound.wav')
            pygame.mixer.music.play()

run_game()