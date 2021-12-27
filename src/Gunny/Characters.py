import pygame

class Character():
    def __init__(self,g_settings, floor):
        self.image = g_settings.character1
        self.rect = self.image.get_rect()
