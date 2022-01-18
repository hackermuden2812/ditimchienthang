import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,folderName,direction,booster,bullets):
        self.image = pygame.transform.smoothscale(pygame.image.load(f'src/Gunny/assets/{folderName}/Idle/idle1.png'),(120,200))
        self.rect = self.image.get_rect()
        self.direction = direction
        self.turn = False
        self.isShooting = True
        self.maxHp = 100
        self.hp=self.maxHp
        self.alive = True
        self.booster = booster
        self.bullets =bullets
    def update (self):
        pass
