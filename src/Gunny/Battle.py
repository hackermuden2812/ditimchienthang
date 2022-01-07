import sys
import pygame
from pygame.constants import K_SPACE, MOUSEBUTTONUP, K_c
from Bullet import Bullet
from HealthBar import HealthBar
from Settings import Settings
import GameFunction as gf
from Players import Player
import time
from clockwise import ClockWise
pygame.init()

class Game:
    def __init__(self):
        self.settings= Settings()
        self.current_fighter = 1
        self.total_fighters = 3
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.powerups = False
        self.powerups_effect = 15
        self.clicked = False
        self.game_over = 0
        self.window = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.set_caption("Gunny")
        self.player1 = Player(120,510,'Player1',100,10,3)
        self.clockwise1 = ClockWise(120,420)

        self.player2 = Player(self.settings.window_width-120,510,'Player1',100,10,3)
        self.clockwise2 = ClockWise(self.settings.window_width-120,420)
        for i in range(len(self.player2.animation_list)):
            for j in range(len(self.player2.animation_list[i])):
                self.player2.animation_list[i][j]= pygame.transform.flip(self.player2.animation_list[i][j],True,False)
                
        self.clock = pygame.time.Clock()
        self.running =True
    def draw_bg(self):
        self.window.blit(self.settings.bg,(0,0))
    def drawText():
        pass
    def run(self):
        while self.running:
            self.clock.tick(self.settings.FPS)
            #tạo background
            self.draw_bg()

            #update Player 1
            self.player1.update()
            self.player1.draw(self.window)

            #update Player 2
            self.player2.update()
            self.player2.draw(self.window)
            

            #update thước bắn
            self.clockwise1.update(self.window,False)
            self.clockwise2.update(self.window,True)
            #đặt các giá trị khi chưa bắn
            self.attack = False
            self.powerups = False
            self.target = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == K_c:
                    self.player1.action=1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True
                else:
                    self.clicked = False
            pygame.display.update()
        pygame.quit()



Game = Game()
Game.run()