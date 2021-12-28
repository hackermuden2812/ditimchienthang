import pygame
from pygame.constants import K_SPACE, KEYDOWN

from Bullet import Bullet
from GameFunction import *
from HealthBar import HealthBar
from Settings import Settings
import GameFunction as gf
from Characters import *
from config import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.g_settings = Settings()
        self.window = pygame.display.set_mode((self.g_settings.window_width, self.g_settings.window_height))
        pygame.display.set_caption("Gunny")
        
        self.bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.player1 = Player('src/Gunny/assets/nv1.png',(200, 490), self.all_sprites, self.bullets)
        self.player2 = Player('src/Gunny/assets/player1.png',(1200, 490), self.all_sprites, self.bullets)
        self.healthBar_a = HealthBar('src/Gunny/assets/redHealthBar.png')
        self.healthBar_b = HealthBar('src/Gunny/assets/blueHealthBar.png')
        self.done = False
        self.clock = pygame.time.Clock()
        self.window.blit(self.g_settings.bg, (0, 0))
        
        self.window.blit(self.healthBar_a.image, (0, 0))
        self.window.blit(pygame.transform.flip(self.healthBar_b.image, True,
                    False), (self.g_settings.window_width-400, 0))

    def run(self):
        while not self.done:
            # dt = time since last tick in milliseconds.
            dt = self.clock.tick(self.g_settings.FPS)/5000
            self.handle_events()
            self.run_logic(dt)
            self.draw()

    # def run_game(self):
    def run_logic(self, dt):
        # self.bullets.pos = self.player1.rect.center()
        self.all_sprites.update(dt)

        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == MOUSEBUTTONDOWN:
                fire() 

    def draw(self):
        # self.window.fill(pygame.Color('gray12'))
        self.all_sprites.draw(self.window)
        pygame.display.flip()
    def fire (self):
        pygame.mixer.music.load('src/Gunny/assets/fireSound.wav')
        pygame.mixer.music.play()
        # self.bullets.pos+= (5,0)
        
if __name__ == '__main__':
    Game().run()
    pygame.quit()
