import pygame
import random
import sys
import math

from pygame.constants import BLEND_ALPHA_SDL2, QUIT
from pygame.sprite import AbstractGroup
from sprites import *
from Gunny.config import *


m=0.5
v0=8
x=120
y=400
gX=5
gY=-9.8
t=0
dt = 0.5
angle =30 * math.pi/180
vX= v0 *math.cos(angle)
vY= v0 *math.sin(angle)
window = pygame.display.set_mode(
            (1200, 500)
        )
window.fill((0,0,0))
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x =x
        self.y=y
        self.m=0.5
        self.image=pygame.image.load('src/Gunny/assets/Player1/Bullet/bullet0.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(34,28))
        self.rect= self.image.get_rect()
        self.rect.center = (x,y)
    def update(self) -> None:
        self.rect.x+=gX*dt/self.m
        self.rect.y+=gY*dt/self.m
        
all_sprites = pygame.sprite.Group()
bullet = Bullet(x,y)
all_sprites.add(bullet)
running = True
while running:
    pygame.init()
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            # sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.draw(window)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
sys.exit()