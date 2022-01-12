import sys
import pygame
from pygame.constants import K_SPACE, MOUSEBUTTONUP
from Bullet import Bullet

from Settings import Settings
import GameFunction as gf
from Characters import Character
import time
class Game:
#Khoi tao game
    def __init__(self) -> None:
        
        pygame.init()
        self.g_settings = Settings()
        #bullet
        self.bullets = Bullet(120,400)
        #Player 1
        self.character_a = Character('Player1', 1,3,self.bullets)
        #Player 2
        self.character_b = Character('Player1', -1,3,self.bullets)
        self.character_b.image= pygame.transform.flip(self.character_b.image,True,False)
        #game clock
        self.clock = pygame.time.Clock()
        self.clock.tick(self.g_settings.FPS)
        #screen
        self.window = pygame.display.set_mode(
            (self.g_settings.window_width, self.g_settings.window_height)
        )
        pygame.display.set_caption("Gunny")

        self.bulletsA = []
        self.bulletsA.append([100,500])
        self.bulletsB = []
        self.bulletsB.append([1200,500])
        

    def draw_bg(self):
        self.window.blit(self.g_settings.bg,(0,0))

    #Game Loop   
    def run_game(self):

        while True:   
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.fire(self.bulletsA,self.character_a,self.character_b)
                    pass
            
            self.draw_bg()        
            self.window.blit(self.character_a.image,(0,390))
            self.window.blit(self.character_b.image,(self.g_settings.window_width-120,390))
            
            pygame.display.update()
    def fire (self,bullets,player,enemy):
        enemy.turn = False
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                while player.isShooting:
                    while bullets[len(bullets)-1][0] <= 1200 or bullets[len(bullets)-1][0] >= 0:
                        bullets.append([5*player.direction*(len(bullets)-1),500])
                for bullet in bullets:                
                    self.window.blit(self.bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
            print(bullet)           
            if event.type == pygame.MOUSEBUTTONUP:
                player.turn = False
                player.isShooting= False
                enemy.turn == True

        
        pygame.mixer.init()
        pygame.mixer.music.load('src/Gunny/assets/fireSound.wav')
        pygame.mixer.music.play()

Game = Game()
Game.run_game()