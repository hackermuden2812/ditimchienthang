import pygame, sys
from Settings import Settings
import GameFunction as gf
from Characters import Character

def run_game():
    pygame.init()
    g_settings = Settings()
    character = Character(g_settings,g_settings.floor)
    clock = pygame.time.Clock()
    clock.tick(g_settings.FPS)
    window = pygame.display.set_mode(
        (g_settings.window_width, g_settings.window_height)
    )
    pygame.display.set_caption("Gunny")
    window.blit(g_settings.bg,(0,0))
    window.blit(g_settings.floor,(0,850))
    window.blit(character.image,(0,0))
    while True:
        gf.check_events()
        gf.update_screen(g_settings, window)

run_game()
