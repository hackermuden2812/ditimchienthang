from re import X
from threading import local
# from typing_extensions import Self
import pygame
import sys

pygame.init()
window = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()
global x
x=0.2

#bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, speed, angle,side):
        super().__init__()
        self.side = side
        self.surface = surface
        self.speed = speed
        self.angle = angle
        self.gravityChange = 0.5
        self.direction = pygame.math.Vector2(0,0) # dieu huong bang vecto
        
        self.image = pygame.transform.smoothscale(pygame.image.load('src/Gunny/Assets/Player1/Bullet/bullet4.png'),(40,34))
        self.rect = self.image.get_rect(topleft= (100, 400))
        
        self.shoot = False
    
    def fly_with_speed(self):
        self.rect.x += self.speed * self.side
        self.gravity()
    
    def gravity(self):
        self.direction.y += self.gravityChange
        self.rect.y += self.direction.y
    
    def shot(self):
        self.direction.y -= self.angle
        self.rect.y += self.direction.y
        self.shoot = True
        
    
    def update(self):
        if self.shoot == True:
            self.fly_with_speed()
        if self.rect.y >500:
            self.kill()
        self.surface.blit(self.image, self.rect)


#fire power bar
class Rect ():
    def __init__(self) -> None:
        self.maxPower = 20
        self.currentPower = 1
        self.side = 1
        self.change = 0.2
        self.des = False
        self.running = True
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
        pygame.draw.rect(surface,(255,0,255),(0,105,400*self.currentPower/self.maxPower,30))
        return self.currentPower

    def draw(self,surface):
        # pygame.draw.rect(surface,(255,200,0),(0,250,400,30))
        pygame.draw.rect(surface,(225,255,255),(0,100,400,40))
        pygame.draw.rect(surface,(255,0,255),(0,105,400*self.currentPower/self.maxPower,30))


class DirectionBar():
    def __init__(self,x,y):
        #đặt vị trí cho thanh góc bắn :
        self.x = x
        self.y = y
        self.barPos = [ 
                        (x+27*2,y-2),
                        (x+26*2,y-5),
                        (x+25*2,y-8),
                        (x+23*2,y-12),    
                        (x+21*2,y-14),
                        (x+18*2,y-15),
                        (x+15*2,y-17),
                        (x+13*2,y-19),
                        (x+11*2,y-21) 
                    ]
        self.curPos= 0 
        self.des = False
        self.side = 1
    def update(self):
        if self.des == False:
            self.curPos += self.side
        else :
            self.side =-1
            self.curPos += self.side
        if self.curPos <0 :
            self.curPos = 0
        if self.curPos > 8:
            self.curPos = 8
        return self.curPos

        
    def down(self):
        self.curPos -= 1
        if self.curPos < 0 :
            self.curPos = 0
        elif self.curPos >8:
            self.curPos = 8
        pygame.draw.line(window,(0,0,0),(self.x,self.y), self.barPos[self.curPos],3)
    def draw(self):
        pygame.draw.line(window,(0,0,0),(self.x,self.y), self.barPos[self.curPos],3)
        

        
        
    
        
bar = Rect()
bullet = Bullet(window,5,15,1)
dir = DirectionBar(100,400)
running = True
pressed = False
while running:
    clock.tick(60)
    window.blit(pygame.transform.smoothscale(pygame.image.load('src/Gunny/assets/bg1.jpg'),(1200,600)),(0,0))
    bar.draw(window)
    bar.update()
    dir.draw()
    bullet.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_SPACE] and not pressed :
        bar.paused(window)
        print('press '+str(bar.currentPower))
        pressed = True
        bullet.speed = bar.currentPower
        bullet.angle = dir.curPos *2
        print('%i %i', bullet.speed,bullet.direction.y)
        bullet.shot()
    if keyPressed[pygame.K_UP]:
        # dir.des = False
        # dir.update()
        dir.curPos += 1
        if dir.curPos >8:
            dir.curPos = 8
        
        print(dir.curPos)
    if keyPressed[pygame.K_DOWN]:
        # dir.des= True
        # dir.update()
        dir.curPos -= 1
        if dir.curPos < 0:
            dir.curPos = 0  
        
        print(dir.curPos)

    # dir.curPos =0

    pygame.display.update()

