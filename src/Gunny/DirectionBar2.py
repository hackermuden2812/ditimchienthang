import pygame
import math
from config import *
pygame.init()
barX=30
barY = 45
groundHeight = 0.9 * HEIGHT
class DirectionBar2():
    def __init__(self,x,y):
        #đặt vị trí cho thanh góc bắn :
        self.x = x
        self.y = y
        self.barPos = [ 
                        (x-27*2,y-2),
                        (x-26*2,y-5),
                        (x-25*2,y-8),
                        (x-23*2,y-12),    
                        (x-21*2,y-14),
                        (x-18*2,y-15),
                        (x-15*2,y-17),
                        (x-13*2,y-19),
                        (x-11*2,y-21) 
                    ]

        self.curPos= 0
        # self.rect= self.image.get_rect()
        # self.rect.center = (x, y)
    def up(self):
        self.curPos += 1
        if self.curPos < 0 :
            self.curPos = 0
        elif self.curPos >8:
            self.curPos = 8
        self.draw()
        
    def down(self):
        self.curPos -= 1
        if self.curPos < 0 :
            self.curPos = 0
        elif self.curPos >8:
            self.curPos = 8
        self.draw()
        
    def draw(self):
        pygame.draw.line(SCREEN,BLACK,(self.x,self.y), self.barPos[self.curPos],3)
        
    
        