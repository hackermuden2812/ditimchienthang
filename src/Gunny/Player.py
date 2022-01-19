import math
import pygame
import random
from DirectionBar1 import DirectionBar1
from ShotPower import ShotPower
from config import *
from Bullet import Bullet
from DirectionBar2 import DirectionBar2

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name, maxHp, strength, powerups,side):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.name = name
        self.maxHp = maxHp
        self.hp = maxHp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 1  # 0:đứng yên, 1:đánh, 2:bị thương, 3:chết
        self.update_time = pygame.time.get_ticks()
        # tải ảnh đỨng
        temp_list = []
        for i in range(1,11):
            img = pygame.image.load(
                f'src/Gunny/assets/{self.name}/Idle/Idle ({i}).png')
            img = pygame.transform.smoothscale(img, (280, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # tải các frame bắn
        temp_list = []
        for i in range(1,11):
            img = pygame.image.load(
                f'src/Gunny/assets/{self.name}/Attack/Attack ({i}).png')
            img = pygame.transform.smoothscale(img, (280, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #tải các frame nv bị thương
        temp_list = []
        for i in range(1,11):
            img = pygame.image.load(
                f'src/Gunny/assets/{self.name}/Hurt/Hurt ({i}).png')
            img = pygame.transform.smoothscale(img, (280, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # tải các frame nv chết
        temp_list = []
        for i in range(1,11):
            img = pygame.image.load(
                f'src/Gunny/assets/{self.name}/Death/Death ({i}).png')
            img = pygame.transform.smoothscale(img, (280, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        if side == -1:
            for i in range(len(self.animation_list)):
                for j in range(len(self.animation_list[i])):
                    self.animation_list[i][j]= pygame.transform.flip(self.animation_list[i][j],True,False)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.bullet = Bullet(f'src/Gunny/assets/{self.name}/bullet.png',SCREEN,self.rect.center[0],self.rect.center[1],5,15,side)
        if side == -1:
            self.dir=DirectionBar2(self.rect.topleft[0]+ 50,self.rect.topleft[1])
            self.shotPower = ShotPower(self.rect.bottomleft[0],self.rect.bottomleft[1]+30)
        elif side ==1:
            self.dir=DirectionBar1(self.rect.topright[0]-100,self.rect.topright[1])
            self.shotPower = ShotPower(self.rect.bottomleft[0]+50,self.rect.bottomleft[1]+30)

    def resetBullet(self,bullet):
        pass
    def update(self):
        animation_cooldown = 100
        # xử lí animation
        # update hình ảnh player
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # Khi đến frame cuối của animation sẽ reset frame về 0
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self):
        
        # set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    def hurt(self):
        
        # set variables to attack animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    def takeDamage (self, target):
        damage = self.strength
        # deal damage to enemy
        rand = random.randint(-3, 3)
        target.hp -= (damage +rand)
        # run enemy hurt animation

        # check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()

    def death(self):
        # set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_powerups
        self.hp = self.maxHp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
