import pygame
import sys

pygame.init()
# window = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()


class ShotPower():
    def __init__(self,x,y):
        self.maxPower = 20
        self.currentPower = 1
        self.side = 1
        self.change = 0.2
        self.des = False
        self.running = True
        self.x=x
        self.y = y
    def update(self):
        if self.running:
            if self.des == False:
                self.currentPower += self.side*self.change 
            else:
                self.side = -1
                self.currentPower += self.side*self.change 

            if self.currentPower >20:
                self.currentPower =20
                self.des = True
            if self.currentPower < 0:
                self.currentPower =0
                self.des = False
                self.side=1
            # print(400*self.currentPower/self.maxPower)
        
    def paused(self,surface):
        self.running = False
        pygame.draw.rect(surface,(255,0,255),(self.x,self.y+5,250*self.currentPower/self.maxPower,30))
        return self.currentPower

    def draw(self,surface):
        # pygame.draw.rect(surface,(255,200,0),(0,250,250,30))
        pygame.draw.rect(surface,(225,255,255),(self.x,self.y,250,40))
        pygame.draw.rect(surface,(255,0,255),(self.x,self.y+5,250*self.currentPower/self.maxPower,30))
