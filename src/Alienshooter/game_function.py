import sys
import pygame
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
        elif event.type == pygame.KEYUP:
               if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
               elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
def update_screen(ai_settings, screen, ship):
     """Cập nhật các ảnh lên trên màn hình và chuyển sang màn hình mới"""
     #Thực hiện vẽ lại màn hình trong mỗi lần lặp
     screen.fill(ai_settings.bg_color)
     ship.blitme()
     #Thực hiện hiển thị màn hình
     pygame.display.flip()