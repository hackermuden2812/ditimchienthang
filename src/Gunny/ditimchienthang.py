import pygame
from Bullet import Bullet
from HealthBar import HealthBar   
from Settings import Settings
import GameFunction as gf
from Characters import Character
class Game :
    def __init__(self) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Character((0, 0), self.all_sprites, self.bullets)
    def run_game():
        pygame.init()
        g_settings = Settings()
        character_a = Character('src/Gunny/assets/nv1.png')
        character_b = Character('src/Gunny/assets/player1.png')
        healthBar_a = HealthBar('src/Gunny/assets/redHealthBar.png')
        healthBar_b = HealthBar('src/Gunny/assets/blueHealthBar.png')
        # bullet = Bullet('src/Gunny/assets/bullet.png',50,390)
        clock = pygame.time.Clock()
        clock.tick(g_settings.FPS)
        window = pygame.display.set_mode(
            (g_settings.window_width, g_settings.window_height)
        )
        pygame.display.set_caption("Gunny")
        
        window.blit(g_settings.bg,(0,0))
        window.blit(character_a.image,(50,390))
        # window.blit(bullet.image,(50,390))
        window.blit(character_b.image,(1200,390))
        window.blit(healthBar_a.image,(0,0))
        window.blit(pygame.transform.flip(healthBar_b.image,True,False),(g_settings.window_width-400,0))
        

        while True:
            gf.check_events()
            gf.update_screen(g_settings, window)

    run_game()
