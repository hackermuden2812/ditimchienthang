from cProfile import run
from dis import Instruction
import math
from platform import python_branch
from re import X
import sys
import pygame
from pygame.constants import K_SPACE, K_UP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_c
from pygame.sprite import spritecollide
from Bullet import Bullet
from Healthbar import HealthBar
from Player import Player
from DirectionBar1 import DirectionBar1
from config import *

from Button import Button
from Bullet import Bullet
from ShotPower import ShotPower


pygame.init()


# tao cac sprtite gr

bullet1_group = pygame.sprite.GroupSingle()
bullet2_group = pygame.sprite.GroupSingle()

#Tạo các item liên quan đến player1
player1 = Player(120,510,'Elf',100,10,3,1)
# clockwise1 = Clockwise()
healthBar1 = HealthBar(100,20,player1.hp,player1.maxHp)
#Tạo các item liên quan đến player2
player2 = Player(WIDTH-120,540,'Knight',100,10,3,-1)
# clockwise2 = Clockwise()
healthBar2 = HealthBar(WIDTH-500,20,player2.hp,player2.maxHp)

class Game:
    bgX = 0
    def __init__(self):
        self.current_player = 1
        self.total_players = 2
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.shooting = False
        self.game_over = 0        
        self.running =True  
        self.pressed = False
        self.status = False
    def getFont(self,size):
        return pygame.font.Font('src/Gunny/assets/EvilEmpire-4BBVK.ttf',size)
    def movingBackground(self,bgX):
        SCREEN.blit(BACKGROUND,(bgX,0))
        SCREEN.blit(BACKGROUND,(bgX+WIDTH,0))
    def paused(self):
        while True :
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.fill((255,255,255))
            optionBack = Button(image=BUTTON_BG, pos=(WIDTH/2, 300), 
                                text_input="BACK", font=self.getFont(50), base_color="Black", hovering_color="White")

            optionBack.changeColor(OPTIONS_MOUSE_POS)
            optionBack.update(SCREEN)
            optionHome = Button(image=BUTTON_BG, pos=(WIDTH/2, 450), 
                                text_input="HOME", font=self.getFont(50), base_color="Black", hovering_color="White")

            optionHome.changeColor(OPTIONS_MOUSE_POS)
            optionHome.update(SCREEN)
            optionQuit = Button(image=BUTTON_BG, pos=(WIDTH/2, 600), 
                                text_input="QUIT", font=self.getFont(50), base_color="Black", hovering_color="White")

            optionQuit.changeColor(OPTIONS_MOUSE_POS)
            optionQuit.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if optionHome.checkForInput(OPTIONS_MOUSE_POS):
                        self.mainMenu()                
                    if optionBack.checkForInput(OPTIONS_MOUSE_POS):
                        self.run()                
                    if optionQuit.checkForInput(OPTIONS_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    def winner(self,player):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            optionPlay = Button(image=BUTTON_BG, pos=(WIDTH/2, 300), 
                                text_input="PLAY AGAIN", font=self.getFont(50), base_color="Black", hovering_color="White")

            optionPlay.changeColor(OPTIONS_MOUSE_POS)
            optionPlay.update(SCREEN)
            optionHome = Button(image=BUTTON_BG, pos=(WIDTH/2, 450), 
                                text_input="QUIT", font=self.getFont(50), base_color="Black", hovering_color="White")

            optionHome.changeColor(OPTIONS_MOUSE_POS)
            optionHome.update(SCREEN)
            optionQuit = Button(image=BUTTON_BG, pos=(WIDTH/2, 600), 
                                text_input="QUIT", font=self.getFont(50), base_color="Black", hovering_color="White")

            optionQuit.changeColor(OPTIONS_MOUSE_POS)
            optionQuit.update(SCREEN)

            winner = self.getFont(45).render(f'{player.name} WIN', True, "Black")
            winnerRect = winner.get_rect(center=(WIDTH/2, 150))
            SCREEN.blit(winner,winnerRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if optionHome.checkForInput(OPTIONS_MOUSE_POS):
                        self.mainMenu()                
                    if optionPlay.checkForInput(OPTIONS_MOUSE_POS):
                        player1.reset()
                        player2.reset()
                        self.run()                
                    if optionQuit.checkForInput(OPTIONS_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    def instruction(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill((255,255,255))

            instruction1 = self.getFont(45).render("Use the up and down arrow key to adjust the direction bar.", True, "Black")
            instruction2 = self.getFont(45).render("Use the Spacebar to meter shot power and then shoot.", True, "Black")
            instructionRect1 = instruction1.get_rect(center=(WIDTH/2, 260))
            SCREEN.blit(instruction1, instructionRect1)
            instructionRect2 = instruction2.get_rect(center=(WIDTH/2, 360))
            SCREEN.blit(instruction2, instructionRect2)

            OPTIONS_BACK = Button(image=BUTTON_BG, pos=(WIDTH/2, 460), 
                                text_input="BACK", font=self.getFont(50), base_color="Black", hovering_color="White")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.mainMenu()

            pygame.display.update()
    def mainMenu(self):
        bgX=0
        while True:
            # SCREEN.blit(BACKGROUND,(0,0))
            # self.draw_bg()
            bgX -= 1
            self.movingBackground(bgX)
            if bgX <= -WIDTH:
                bgX =0

            mousePos = pygame.mouse.get_pos()
            mainMenuText = self.getFont(75).render("MAIN MENU", True, (133,100,0))
            mainMenuRect = mainMenuText.get_rect(center=(WIDTH/2, 150))
            SCREEN.blit(mainMenuText, mainMenuRect)


            startButton = Button(image=BUTTON_BG, pos=(WIDTH / 2, 300), 
                            text_input="PLAY", font=self.getFont(50), base_color="#d7fcd4", hovering_color="White")
            instrButton = Button(image=BUTTON_BG, pos=(WIDTH / 2, 450), 
                                text_input="INSTRUCTION", font=self.getFont(50), base_color="#d7fcd4", hovering_color="White")
            quitButton = Button(image=BUTTON_BG, pos=(WIDTH / 2, 600), 
                                text_input="QUIT", font=self.getFont(50), base_color="#d7fcd4", hovering_color="White")
            for button in [startButton, instrButton, quitButton]:
                button.changeColor(mousePos)
                button.update(SCREEN)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startButton.checkForInput(mousePos):
                        self.run()
                    if instrButton.checkForInput(mousePos):
                        self.instruction()
                    if quitButton.checkForInput(mousePos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
    def draw_bg(self):
        SCREEN.blit(BACKGROUND,(0,0))
    def run(self):
        players_sprites = pygame.sprite.Group()
        players_sprites.add(player1)
        players_sprites.add(player2)
        bullet_sprites = pygame.sprite.Group()
        while self.running:
            CLOCK.tick(FPS)
            #tạo background
            self.draw_bg() 
            players_sprites.update()
            bullet_sprites.update()
            players_sprites.draw(SCREEN)
            bullet_sprites.draw(SCREEN)

            #update thanh HP
            healthBar1.draw(player1.hp,SCREEN,(GREEN ))
            healthBar2.draw(player2.hp,SCREEN,(BLUE))
            
            #đặt các giá trị khi chưa bắn
            self.attack = False
            self.powerups = False
            self.target = None
            
            self.current_player = player2.bullet.update(self.current_player)        
            self.current_player = player1.bullet.update(self.current_player)

            if self.current_player == 1:
                player1.dir.draw()
                player1.shotPower.draw(SCREEN)
                player1.shotPower.update()
                if self.shooting:
                    player1.attack()
                    if player1.bullet.rect.colliderect(player2.rect):
                        print('Check')
                        player2.hurt()
                        player1.takeDamage(player2)   
                        player1.bullet.rect.x = player1.rect.center[0]
                        player1.bullet.rect.y = player1.rect.center[1]
                        self.shooting = player1.bullet.shoot
                    # if player1.bullet.check_collision_border():
                    #     # self.current_player += 1
                    self.shooting = player1.bullet.shoot
                    print(self.shooting)
                    
            elif self.current_player == 2:
                player2.dir.draw()
                player2.shotPower.draw(SCREEN)
                player2.shotPower.update()
                if self.shooting:
                    player2.attack()
                    if player2.bullet.rect.colliderect(player2.rect):
                        player1.hurt()
                        player2.takeDamage(player1)   
                        player2.bullet.rect.x = player2.rect.center[0]
                        player2.bullet.rect.y = player2.rect.center[1]
                        # self.current_player -= 1
                        self.shooting = player2.bullet.shoot
                    # if player2.bullet.check_collision_border():
                    #     # self.current_player -= 1
                    
                    self.shooting = player2.bullet.shoot
                    print(self.shooting)
            
            print(self.current_player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_UP]:
                if self.current_player == 1:
                    player1.dir.up()
                    # player1.dir.draw()
                    print('Press 1') 
                else :
                    player2.dir.up()
                    # player2.dir.draw()

            elif keyPressed[pygame.K_DOWN]:
                if self.current_player == 1:
                    player1.dir.down()
                    # player1.dir.draw()
                    print('Press 2')
                else :
                    player2.dir.down()
                    # player2.dir.draw()jjalksdjlaksjd
            if keyPressed[pygame.K_SPACE] and not self.pressed:
                print('Press space')

                self.shooting = True
                if not self.pressed:
                    if self.current_player == 1:
                        player1.shotPower.paused(SCREEN)
                        self.pressed = True 
                        player1.bullet.speed = player1.shotPower.currentPower
                        player1.bullet.angle = player1.dir.curPos *2
                        player1.bullet.shot()

                    if self.current_player == 2:
                        player2.shotPower.paused(SCREEN)
                        self.pressed = True 
                        player2.bullet.speed = player2.shotPower.currentPower
                        player2.bullet.angle = player2.dir.curPos *2
                        player2.bullet.shot()
            elif not  keyPressed[pygame.K_SPACE] :
                self.shooting = False
            if keyPressed[pygame.K_ESCAPE]:
                self.paused()
            pygame.display.flip()
        pygame.quit()



Game = Game()
Game.mainMenu()