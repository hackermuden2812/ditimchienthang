import pygame
from pygame.constants import K_SPACE, MOUSEBUTTONUP
from HealthBar import HealthBar
from Settings import Settings
import GameFunction as gf
from Characters import Character
import time

#Khoi tao game
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
bulletsA.append([100,500])
bulletsB = []
bulletsB.append([1200,500])
bullets=[]
count =0
#Game Loop   
def run_game():

    while True:        
        gf.update_screen(g_settings, window)
        if character_a.turn:
            fire(bulletsA,character_a,character_b)
            
        elif character_b.turn:
            fire(bulletsB,character_b,character_a)
            
        window.blit(g_settings.bg,(0,0))          
        window.blit(character_a.image,(0,390))
        window.blit(character_b.image,(g_settings.window_width-120,390))
        window.blit(healthBar_a.image,(0,0))
        window.blit(pygame.transform.flip(healthBar_b.image,True,False),(g_settings.window_width-400,0))
def fire (bullets,player,enemy):
    enemy.turn = False
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            while player.isShooting:
                while bullets[len(bullets)-1][0] <= 1200 or bullets[len(bullets)-1][0] >= 0:
                    bullets.append([5*player.direction*(len(bullets)-1),500])
            for bullet in bullets:                
                window.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
        print(bullet)           
        if event.type == pygame.MOUSEBUTTONUP:
            player.turn = False
            player.isShooting= False
            enemy.turn == True

    
    pygame.mixer.init()
    pygame.mixer.music.load('src/Gunny/assets/fireSound.wav')
    pygame.mixer.music.play()

run_game()