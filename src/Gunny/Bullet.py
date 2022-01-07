import pygame
class Bullet():
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.bullet=[]
        self.bulletFrameIndex =0
        self.update_time = pygame.time.get_ticks()
        for i in range (5):
            bulletImg= pygame.image.load(f'src/Gunny/assets/Player1/Bullet/bullet{i}')
            bulletImg=pygame.transform.smoothscale(bulletImg, (34,28))
            self.bullet.append(bulletImg)
        self.bulletImage =self.bullet[self.bulletFrameIndex]
        self.rect = self.bulletImage.get_rect()
        self.rect.center = (x,y)
    def update(self):
        animation_cooldown = 100
        self.bulletImage = self.bullet[self.bulletFrameIndex]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.bulletFrameIndex+=1
        if self.bulletFrameIndex > len(self.bullet):
            self.frame_index=0
    def draw(self,window):
        window.blit(self.bulletImage, self.rect)
