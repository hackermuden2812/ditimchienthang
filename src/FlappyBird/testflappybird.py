import pygame
import os
import sys
import random
#Tạo vòng lặp vô hạn Floor
pygame.init()
def draw_Floor():
    window.blit(floor,(floor_x_pos,650))
    window.blit(floor,(floor_x_pos+432,650))
#Tạo ống
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos - 650))
    return bottom_pipe, top_pipe 
def move_pipe(pipes):
    for pipe in pipes : 
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes :
        if pipe.bottom >= 600:
            window.blit(pipe_surface, pipe)
        else :
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            window.blit(flip_pipe, pipe)
#Xử lý va chạm
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3, 1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird,new_bird_rect
def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)), True, (255,255,255))
        score_rect = score_surface.get_rect(center = (216, 100))
        window.blit(score_surface, score_rect)
    if game_state == 'game over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255)) 
        score_rect = score_surface.get_rect(center = (216, 100))
        window.blit(score_surface, score_rect)
        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255,255,255))
        high_score_rect = score_surface.get_rect(center = (216, 630))
        window.blit(high_score_surface, high_score_rect)
def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score
#Set màn hình chơi game
window = pygame.display.set_mode((432,768))
#Đặt tên game
pygame.display.set_caption("Đi tìm chiến thắng!")
#Set FPS cho game
clock = pygame.time.Clock()
#tạo font
game_font = pygame.font.Font('FileGame/04B_19.ttf', 40)
#Set trọng lực
gravity = 0.25
bird_movement = 0   
game_active = True
score = 0
high_score = 0
#Set asset cho game
bg = pygame.image.load('FileGame/assets/background-night.png').convert()
floor = pygame.image.load('FileGame/assets/floor.png').convert()
# bird = pygame.image.load('FileGame/assets/yellowbird-midflap.png').convert_alpha()
bird_down = pygame.transform.scale2x(pygame.image.load('FileGame/assets/yellowbird-downflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('FileGame/assets/yellowbird-upflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('FileGame/assets/yellowbird-midflap.png').convert_alpha())
bird_list = [bird_down,bird_mid, bird_up]
bird_index = 0
bird = bird_list[bird_index]
pipe_surface = pygame.image.load('FileGame/assets/pipe-green.png').convert()
#Tạo ống
pipe_list = []
pipe_height = [200,300,400]
#Scale asset
bg = pygame.transform.scale2x(bg)
floor = pygame.transform.scale2x(floor)
# bird = pygame.transform.scale2x(bird)
pipe_surface = pygame.transform.scale2x(pipe_surface)
floor_x_pos = 0
#Tạo timer cho bird
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)
#Tạo timer
spawnpipe = pygame.USEREVENT
#Sau 1.2s sẽ tạo ra 1 ống mới
pygame.time.set_timer(spawnpipe, 1200)
bird_rect = bird.get_rect(center = (100,384))
#Tạo font cho game
pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans", 30)
#Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('FileGame/assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(216,384))
#while loop của trò chơi
while True:
    #Làm game tắt khi nhấn vào dấu X
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Nhấn space là chim bay lên
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement =- 11
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
        
    #Set asset theo trục tọa độ
    window.blit(bg,(0,0))
    if game_active:
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display('main game')
        #Làm con chim cứ auto rớt xuống
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        window.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)
    else:
        window.blit(game_over_surface, game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game over')
    #Làm cho sàn di chuyển lùi
    floor_x_pos -= 1
    draw_Floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)