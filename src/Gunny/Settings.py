import pygame


class Settings():

    def __init__(self):
        self.window_width = 1400
        self.window_height = 800
        self.FPS = 120
        self.bg = pygame.transform.smoothscale(pygame.image.load('assets/bg1.jpg'),(self.window_width,self.window_height))  
        # self.floor = pygame.image.load('Assets/Floor.png')

