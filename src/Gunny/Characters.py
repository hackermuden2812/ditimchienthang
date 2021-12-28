import pygame
from Bullet import Bullet 
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, all_sprites, bullets):
        super().__init__()
        self.image = pygame.image.load('src/Gunny/assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets
        self.bullet_timer = .1

    def update(self, dt):
        self.rect.center = pygame.mouse.get_pos()

        mouse_pressed = pygame.mouse.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.
            if mouse_pressed[0]:  # Left mouse button.
                # Create a new bullet instance and add it to the groups.
                Bullet(pygame.mouse.get_pos(), self.all_sprites, self.bullets)
                self.bullet_timer = .1  # Reset the timer.
        
        
