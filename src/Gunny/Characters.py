import pygame

class Character():
    def __init__(self,fileName,direction):
        self.image = pygame.transform.smoothscale(pygame.image.load(fileName),(120,200))
        self.rect = self.image.get_rect()
        self.direction = direction
        self.turn = False
        self.isShooting = True
