import pygame
from config import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,path, surface,x,y, speed, angle,side):
        super().__init__()
        self.side = side
        self.surface = surface
        self.speed = speed
        self.angle = angle
        self.pos = (x,y)
        self.direction = pygame.math.Vector2(0,0) # dieu huong bang vecto
        
        self.image = pygame.transform.smoothscale(pygame.image.load(path),(40,34))
        if side == -1 :
            self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(center= (x, y))
        
        self.shoot = False
    
    def fly_with_speed(self):
        self.rect.x += self.speed * self.side
        self.gravity()
    
    def gravity(self):
        self.direction.y += 0.5
        self.rect.y += self.direction.y
    
    def shot(self): 
        self.direction.y -= self.angle
        self.rect.y += self.direction.y
        self.shoot = True
        
    def check_collision_border(self, current_player):
        bullet_x = self.rect.x
        bullet_y = self.rect.y
        
        if (bullet_x < 0 or bullet_x > WIDTH) or (bullet_y > HEIGHT): 
            self.rect.x = 100
            self.rect.y = 400
            self.shoot = False
            if current_player == 1:
                current_player += 1
            else:
                current_player -= 1
        return current_player
    def update(self, current_player):
        if self.shoot == True:
            self.fly_with_speed()
        self.surface.blit(self.image, self.rect)
        current_player = self.check_collision_border(current_player)
        return current_player