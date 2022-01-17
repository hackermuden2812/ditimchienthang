import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, speed, angle,side):
        super().__init__()
        self.side = side
        self.surface = surface
        self.speed = speed
        self.angle = angle
        
        self.direction = pygame.math.Vector2(0,0) # dieu huong bang vecto
        
        self.image = pygame.transform.smoothscale(pygame.image.load('src/Gunny/Assets/Player1/Bullet/bullet4.png'),(40,34))
        self.rect = self.image.get_rect(topleft= (100, 400))
        
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
        
    
    def update(self):
        if self.shoot == True:
            self.fly_with_speed()
        self.surface.blit(self.image, self.rect)