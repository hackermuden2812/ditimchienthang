import pygame

WIDTH= 1400
HEIGHT= 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND = pygame.transform.smoothscale(pygame.image.load('src/Gunny/assets/bg1.jpg'),(WIDTH,HEIGHT))  
pygame.display.set_caption("Gunny")      
CLOCK = pygame.time.Clock()
FPS = 60

#color 
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
BLUE = (24, 0, 255)