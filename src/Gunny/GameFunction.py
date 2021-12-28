import sys
import pygame
import Bullet
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN

from config import WIDTH
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            
            fire()

def update_screen(g_settings, screen):
     """Cập nhật các ảnh lên trên màn hình và chuyển sang màn hình mới"""
     #Thực hiện vẽ lại màn hình trong mỗi lần lặp
     #Thực hiện hiển thị màn hình
     pygame.display.flip()

def fire ():
    pygame.mixer.music.load('src/Gunny/assets/fireSound.wav')
    pygame.mixer.music.play()
    bullet = Bullet('src/Gunny/assets/bullet.png')
    bullets =[]

    for b in range(len(bullets)):
        bullets[0][b] +=5
    for bullet in bullets[:]:
        if bullet[1] > WIDTH:
            bullets.remove(bullet)
    for bullet in bullets:
        screen.blit(bullet, pygame.Rect(bullet[0], bullet[1], 0, 0))
    pygame.display.flip()


    