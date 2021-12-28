import pygame
class Bullet():
    def __init__(self,fileName):
        self.image = pygame.transform.smoothscale(pygame.image.load(fileName),(100, 50))
        self.rect = self.image.get_rect()
