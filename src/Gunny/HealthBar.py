import pygame
from config import *
class HealthBar():
    def __init__(self, x, y, hp, maxHp):
        self.x = x
        self.y = y
        self.hp =hp
        self.maxHp =maxHp


    def draw(self, hp,window,hpColor):
        self.hp = hp
        #tính tỉ lệ HP còn lại
        ratio = self.hp / self.maxHp
        pygame.draw.rect(window, RED, (self.x, self.y, 400, 50))
        pygame.draw.rect(window, hpColor, (self.x, self.y, 400 * ratio, 50))