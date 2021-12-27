import pygame
import random
import sys
from sprites import *
from config import *

class Game :
    def __init__(self) :
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.score = 0
        self.font = pygame.font.SysFont("Robus", 25)
        pygame.display.set_caption('Gunbound')
        self.running = True

        # archers = pygame.image.load('src/assets/nv7.png').convert_alpha()
        # robot = pygame.image.load('src/assets/nv1.png').convert_alpha()
        # archers = pygame.transform.scale(archers,(100,80))
        # robot = pygame.transform.scale(robot,(100,80))

        # bg=pygame.image.load('src/assets/bg1.jpg').convert_alpha()
        # bg = pygame.transform.scale2x(bg)
    def newGame(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.attack=pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.LayeredUpdates()
        self.player1 = Player(self,1,2)
        self.player2 = Player(self,1,2)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
                self.playing=False  
            

    def update(self):
        #game loop update
        self.all_sprites.update()
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    def main(self):
        #game loop
        while self.playing:
            self.event()
            self.update()
            self.draw()
        self.running= False
        
    def gameOver(self):
        pass
    def introScreen(self):
        pass
game = Game()
game.introScreen()
game.newGame()
while game.running :
    game.main()
    game.gameOver()
pygame.quit()
sys.exit()