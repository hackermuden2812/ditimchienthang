# keys = pygame.key.get_pressed()
# if character_a.turn:
#     bulletsA.append([bulletsA[count][0] + 5 * character_a.direction,500])
#     count+=1
#     for bullet in bulletsA[:]:
#         if bullet[0] < 0:
#             bulletsA.remove(bullet)
#     for bullet in bulletsA:
#         window.blit(bulletpicture, pygame.Rect(
#             bullet[0], bullet[1], 0, 0))

#     character_a.turn = False
#     character_b.turn = True
# elif character_b.turn:
#     bulletsB.append([bulletsB[count][0] + 5 * character_a.direction,500])
#     count+=1
#     for bullet in bulletsB[:]:
#         if bullet[0] < 0:
#             bulletsB.remove(bullet)
#     for bullet in bulletsB:
#         window.blit(pygame.transform.flip(bulletpicture,True,False,(0,500)))
#         window.blit(bulletpicture, pygame.Rect(
#             bullet[0], bullet[1], 0, 0))
#     character_a.turn = True
#     character_b.turn = False
import pygame 
from pygame.constants import K_RIGHT
vec = pygame.math.Vector2

WIDTH = 1000
HEIGHT = 800
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector Basics")
clock = pygame.time.Clock()
vec = pygame.math.Vector2

def draw_text(text, size, color, x, y, align="nw"):
    font_name = pygame.font.match_font('hack')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "nw":
        text_rect.topleft = (x, y)
    if align == "ne":
        text_rect.topright = (x, y)
    if align == "sw":
        text_rect.bottomleft = (x, y)
    if align == "se":
        text_rect.bottomright = (x, y)
    if align == "n":
        text_rect.midtop = (x, y)
    if align == "s":
        text_rect.midbottom = (x, y)
    if align == "e":
        text_rect.midright = (x, y)
    if align == "w":
        text_rect.midleft = (x, y)
    if align == "center":
        text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('src/Gunny/assets/Player1/Bullet/bullet0.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, 0)
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.pos = vec(120, 450)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rot = 0
        self.rot_speed = 90
        self.rect.center = self.pos

    def get_keys(self):
        keys = pygame.key.get_pressed()
        self.rot_speed = 0
        self.acc = vec(0, 0)
        if keys[pygame.K_LEFT]:
            self.rot_speed =90
        elif keys[K_RIGHT]:
            self.rot_speed = -90
       
        
    def update(self, dt):
        self.get_keys()
        self.rot += self.rot_speed * dt
        self.rot = self.rot % 360
        self.image = pygame.transform.rotate(self.image_clean, self.rot)
        self.rect = self.image.get_rect()
        self.acc = self.acc.rotate(-self.rot)
        self.vel += self.acc * dt
        self.pos += self.vel * dt + 0.5 * self.acc * dt**2
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.center = self.pos
        

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    dt = clock.tick(FPS) / 1000
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    # Update
    all_sprites.update(dt)
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text("Rot: {:.2f}".format(player.rot), 18, WHITE, 10, 10, align="nw")
    pygame.display.flip()

pygame.quit()