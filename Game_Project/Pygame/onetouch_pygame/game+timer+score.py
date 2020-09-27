
#--------- Add Timer and Counting Score ---------#
# ------------- Using pygame.camera -------------#
#------------- window scale 1000x700 ------------#

import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#rgb color
black = (0,0,0)
red = (161, 0, 0)
white = (250,250,250)

#font
text_font1 = pygame.font.Font('freesansbold.ttf', 80)
text_font2 = pygame.font.Font('freesansbold.ttf', 30)
text_font3 = pygame.font.Font('freesansbold.ttf', 20)

pygame.display.set_caption('One Touch')
screen = pygame.display.set_mode((1280, 720))
surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )


def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 


#picture bg
image = pygame.image.load(r'C:\software\game\game+gui\ball.jpg') 

#draw button
def draw_rect(color,rect):
    pygame.draw.rect(screen, color , rect)

#show text ONE TOUCH
def text_show(text):
    text_surface = text_font1.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.midright = (750,100)
    screen.blit( text_surface , text_rect )
    return 0

#draw text
def create_text(text,x,y):
    text_surface = text_font2.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = ( x,y )
    screen.blit( text_surface , text_rect )
    return 0

#show text how to play
def text_howto(text,x,y):
    text_surface = text_font3.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit( text_surface , text_rect )
    return 0


#--------------------------------------------------MAIN MENU------------------------------------------------------------#   

def main_menu():

    screen.fill(black)

    screen.blit(image, (200, 400))
    text_show('ONE TOUCH')
    text_howto('** HOW TO PLAY ? : Touch/Click the ball through the camera ',500,400)
    text_howto('when you tap it, there will show your score with coundown timer :P **',500,450)

    button_1 =  pygame.Rect(400,200,200,100)

    pygame.draw.rect(screen, red , button_1)

    create_text('START !',500,250)

    while True:

        mx1, my1 = pygame.mouse.get_pos()
        
        if button_1.collidepoint((mx1, my1)):
            if click:
                game()
    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def game():

    global count_score

    from ball import ball  
    import pygame.camera

    surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

    camera = open_camera()

    obj_ball = ball(surface1)             #สร้างบอลลูกแรก

    count_score = 0

    #Timer
    font = pygame.font.SysFont(None, 45)
    counter = 10
    text = font.render(str(counter), True, white)
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)
    text_rect = text.get_rect()
    text_rect.center = (150,15)

    running= True
    while running:

        img = camera.get_image()
        screen.blit( img , (0,0) )  

        pygame.draw.rect(screen, black , (0,0,1000,60))
        
        create_text('TIME : ' ,80,30)

        screen.blit(text, text_rect.center)
        
        create_text('SCORE :    ' + str(count_score) ,820,30)

        mx2, my2 = pygame.mouse.get_pos()
        button_2 = pygame.Rect(900,650,100,50) #(left,top,width,hight)

        pygame.draw.rect(screen, red , button_2)
        create_text('EXIT',950,675)

        if button_2.collidepoint((mx2, my2)):
            if click:
                score()
                camera.stop()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                counter -= 1
                text = font.render(str(counter), True, white)
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
                    score()
                    camera.stop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    camera.stop()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_ball.is_collided(mx2, my2):
                    surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )          #เหมือนการรีหน้า surface ใหม่เพื่อลบบอลออก
                    count_score += 1
                    pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
                    obj_ball = ball(surface1)
        
        screen.blit( surface1 , (0,0) )

        pygame.display.update()
        clock.tick(60)


def score():

    is_running = True  
    while is_running :

        screen.fill(black)
        screen.blit(image, (200, 400))
        text_show('ONE TOUCH')
        
        mx3,my3 = pygame.mouse.get_pos()
        button_3 = pygame.Rect(400,380,200,100)

        if button_3.collidepoint((mx3, my3)):
            if click:
                main_menu()
        
        pygame.draw.rect(screen, red , button_3)
        create_text('RESTART !',500,440)
        create_text('SCORE :       ' + str(count_score),350,250)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

main_menu()