import pygame

class HealthBar:
    def __init__(self, x, y, hp, maxHp):
        self.x = x
        self.y = y
        self.hp =hp
        self.maxHp =maxHp


    def draw(self, hp,window,hpColor):
        self.hp = hp
        #tính tỉ lệ HP còn lại
        ratio = self.hp / self.max_hp
        pygame.draw.rect(window, (136, 8, 8), (self.x, self.y, 150, 20))
        pygame.draw.rect(window, hpColor, (self.x, self.y, 150 * ratio, 20)) 