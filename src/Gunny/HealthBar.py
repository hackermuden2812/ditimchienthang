import pygame

class HealthBar():
    def __init__(self,fileName,amount = 500):
        self.image = pygame.transform.smoothscale(pygame.image.load(fileName),(400,70))
        self.rect = self.image.get_rect()
        
