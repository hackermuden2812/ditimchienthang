import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(g_settings, screen):
     """Cập nhật các ảnh lên trên màn hình và chuyển sang màn hình mới"""
     #Thực hiện vẽ lại màn hình trong mỗi lần lặp
     #Thực hiện hiển thị màn hình
     pygame.display.flip()