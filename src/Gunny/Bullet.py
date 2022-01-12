import pygame
import math
from config import *
vec = pygame.math.Vector2
gX=0
gY=-9.8
t=0
dt=0.01

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,side):
        pygame.sprite.Sprite.__init__(self)
        self.x =x
        self.y = y
        self.isFlying =False
        if side == 1:
            self.image =pygame.transform.smoothscale(pygame.image.load('src/Gunny/assets/Player1/Bullet/bullet0.png'), (34,28))
        elif side == -1:
            self.image =pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load('src/Gunny/assets/Player1/Bullet/bullet0.png'), (34,28)),True,False)
        # self.pos=(self.x,self.y)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        if self.isFlying == True:
            #update vị trí
            self.rect.x +=10
        if self.rect.x >= WIDTH -120:
            self.kill()
            
    def shot(self):
        self.isFlying = True

    def draw(self):
        SCREEN.blit(self.image, self.rect)
    
