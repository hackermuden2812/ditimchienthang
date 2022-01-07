import pygame
import random
pygame.init()

class Player():
    def __init__(self, x, y, name, max_hp, strength, powerups):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_powerups = powerups
        self.powerups = powerups
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 1  # 0:đứng yên, 1:đánh, 2:bị thương, 3:chết
        self.update_time = pygame.time.get_ticks()
        # tải ảnh đỨng
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'src/Gunny/assets/Player1/Idle/idle{i}.png')
            img = pygame.transform.smoothscale(img, (150, 150))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # tải các frame bắn
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'src/Gunny/assets/Player1/Shoot/shoot{i}.png')
            img = pygame.transform.smoothscale(img, (150, 150))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load death images
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'src/Gunny/assets/Player1/Dead/dead{i}.png')
            img = pygame.transform.smoothscale(img, (150, 150))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
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

    def attack(self, target):
        # deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        # run enemy hurt animation

        # check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()

        # set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        # set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_potions
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self,screen):
        screen.blit(self.image, self.rect)
