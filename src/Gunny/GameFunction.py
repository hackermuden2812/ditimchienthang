import sys
import pygame
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
def check_events(bullets, click):
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if click % 2 == 0:
                bullets.append([0,500])
            else :
                bullets.append([500,500])
            click += 1
def update_screen(g_settings, screen):
     """Cập nhật các ảnh lên trên màn hình và chuyển sang màn hình mới"""
     #Thực hiện vẽ lại màn hình trong mỗi lần lặp
     #Thực hiện hiển thị màn hình
     pygame.display.flip()