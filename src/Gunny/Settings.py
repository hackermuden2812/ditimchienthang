import pygame


class Settings():

    def __init__(self):
        self.window_width = 1920
        self.window_height = 1080
        self.FPS = 120
        self.bg = pygame.image.load('Assets/Background.png')
        self.floor = pygame.image.load('Assets/Floor.png')
        self.character1 = pygame.image.load('Assets/Character1.png')
