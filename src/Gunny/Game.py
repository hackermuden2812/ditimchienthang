import math
import sys
import pygame
from pygame.constants import K_SPACE, K_UP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_c
from pygame.sprite import spritecollide
from Bullet import Bullet
from Healthbar import HealthBar
from Settings import Settings
from Player1 import Player1
from Player2 import Player2
from DirectionBar1 import DirectionBar1
from config import *
pygame.init()


#Tạo các item liên quan đến player1
player1 = Player1(120,510,'Player1',100,10,3)
# clockwise1 = Clockwise()
healthBar1 = HealthBar(100,0,player1.hp,player1.maxHp)
bullet1= Bullet(player1.x,player1.y,1)

#Tạo các item liên quan đến player2
player2 = Player2(WIDTH-120,510,'Player1',100,10,3)
# clockwise2 = Clockwise()
healthBar2 = HealthBar(WIDTH-500,0,player2.hp,player2.maxHp)
bullet2= Bullet(player2.x,player2.y,-1)
#lật ngược (flip) tất cả hình ảnh của Player2 để player2 quay có hướng đối diện player 1
class Game:
    def __init__(self):
        self.current_player = 1
        self.total_players = 2
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.powerups = False
        self.powerups_effect = 15
        self.shooting = False
        self.game_over = 0        
        self.running =True  

    def draw_bg(self):
        SCREEN.blit(BACKGROUND,(0,0))
    def drawText():
        pass
    def run(self):
        players_sprites = pygame.sprite.Group()
        players_sprites.add(player1)
        players_sprites.add(player2)
        bullet_sprites = pygame.sprite.Group()
        while self.running:
            CLOCK.tick(FPS)
            #tạo background
            self.draw_bg()

            #update Player 1
            

            #update Player 2
            

            players_sprites.update()
            bullet_sprites.update()
            players_sprites.draw(SCREEN)
            bullet_sprites.draw(SCREEN)
            #update đạn
            #update thước bắn
            # clockwise1.update(clock.tick(FPS)/1000)
            # clockwise2.update(clock.tick(FPS)/1000 )

            #update thanh HP
            healthBar1.draw(player1.hp,SCREEN,(GREEN))
            healthBar2.draw(player2.hp,SCREEN,(BLUE))
            
            #đặt các giá trị khi chưa bắn
            self.attack = False
            self.powerups = False
            self.target = None

            #player1 attack
            if player1.alive :
                if self.current_player ==1:
                    player1.dir.draw()
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        if self.shooting:
                            bullet_sprites.add(bullet1)                                                  
                            player1.attack()
                            bullet1.shot()
                            # bullet_sprites.update()
                            # bullet_sprites.draw(SCREEN)
                            if bullet1.rect.colliderect(player2.rect):   
                                player1.takeDamage(player2)   
                                bullet1.kill()                    
                                
                            elif bullet1.y > HEIGHT-1000 or bullet1.x > WIDTH:
                                bullet1.kill()
                            self.current_player +=1
                            self.action_cooldown =0

            #player2 attack
            if player2.alive :
                if self.current_player ==2:
                    player2.dir.draw()
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        if self.shooting:
                            bullet_sprites.add(bullet2)
                            player2.attack()
                            player2.takeDamage(player1)
                            self.current_player +=1
                            self.action_cooldown =0
            if self.current_player > self.total_players :
                self.current_player =1
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.type== pygame.K_UP:
                        if self.current_player == 1:
                            player1.dir.curPos+=1
                            print('Press')
                        else :
                            player2.dir.curPos+=1

                    elif event.type == pygame.K_DOWN:
                        if self.current_player == 1:
                            player1.dir.curPos-=1
                            print('Press')
                        else :
                            player2.dir.curPos-=1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('Press')
                    self.shooting = True
                    if self.current_player == 1:
                        bullet1.shot()
                    else :
                        bullet2.shot()
            
                else:
                    self.shooting = False
                    
            

            pygame.display.flip()

        pygame.quit()



Game = Game()
Game.run()