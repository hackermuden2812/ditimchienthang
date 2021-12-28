import pygame
from Bullet import Bullet 
class Player(pygame.sprite.Sprite):
    def __init__(self,imgPath, pos, all_sprites, bullets):
        pygame.init()
        super().__init__()
        self.pos=pos
        self.image = pygame.transform.smoothscale(pygame.image.load(imgPath).convert_alpha(),(120,200))
        self.rect = self.image.get_rect(center=pos)
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets
        self.bullet_timer = .1
        self.health = 100

    def update(self, dt):
        mouse_pressed = pygame.mouse.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.
            if mouse_pressed[0]:  # Left mouse button.
                # Create a new bullet instance and add it to the groups.
                Bullet(self.pos, self.all_sprites, self.bullets)
                self.bullet_timer = .1  # Reset the timer.
        if self.health <= 0:
            self.kill()
        
