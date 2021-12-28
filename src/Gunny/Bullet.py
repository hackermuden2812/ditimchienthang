import pygame
class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        self.image = pygame.Surface((9, 15))

        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(200, 0)
        self.damage = 10

    def update(self, dt):
        # Add the velocity to the position vector to move the sprite.
        self.pos += self.vel * dt *100
        self.rect.center = self.pos  # Update the rect pos.
        if self.rect.centerx <= 0:
            self.kill()