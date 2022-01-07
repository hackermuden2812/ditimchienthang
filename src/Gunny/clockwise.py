import pygame
import math

pygame.init()


class ClockWise:
    def __init__(self, cx, cy) -> None:
        self.cx = cx
        self.cy = cy
        self.step = 0
        self.anglePerStep = .05
        self.lineLen = 100
        self.angle = 0

    def update(self, window,reverse):

        self.angle +=self.step * self.anglePerStep
        if reverse :
            self.angle = -self.angle
        
        if self.angle > math.pi /2:
            self.angle= math.pi/2
            self.angle = -self.angle
            x = self.lineLen / 2.0 * math.sin(self.angle)
            y = self.lineLen / 2.0 * math.cos(self.angle)
            pygame.draw.line(window, (0, 0, 0),(self.cx, self.cy), (self.cx + x, self.cy+y), 3)

        if(self.angle < 0):
            self.angle=0
            x = self.lineLen / 2.0 * math.sin(self.angle)
            y = self.lineLen / 2.0 * math.cos(self.angle)
            pygame.draw.line(window, (0, 0, 0),(self.cx, self.cy), (self.cx + x, self.cy+y), 3)

