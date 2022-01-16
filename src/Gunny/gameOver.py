
import pygame
 
pygame.init()

# set window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gunny')
bg = pygame.image.load('D:\Trên trường\Lập trình nâng cao - Python\ditimchienthang\src\Gunny\Assets\Background-game.jpg')

font = pygame.font.SysFont(None, 50)


# hàm tạo button
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w , h))
    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y)) 


def start():
    print("Ok, let's go")
 
def menu():
    screen.blit(bg,(0,0))
    """ This is the menu that waits you to click the s key to start """
    
    text = font.render('GAME OVER', True, (255,0,0) , (0,128,255))
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (400, 180)
    #Add this in infinite loop.
    #To clear everything on screen
    screen.blit(text, textRect)

    # tạo button
    b1 = button(screen, (430, 400), "Quit me!", 35, "red on yellow")
    b2 = button(screen, (250, 400), "Play again!", 35, "white on green")
    while True:
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check when you click if the coordinates of the pointer are in the rectangle of the buttons
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()

menu()