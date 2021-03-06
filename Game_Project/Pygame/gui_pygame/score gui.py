#Game Progect : ONE TOUCH (Pygame & Python Arcade)
#Blog Update : https://s6201012620139.blogspot.com/2020/09/one-touch-game-project-010123131.html
#student id : 1)นางสาวหทัยพัทร ชำนินวล 6201012620244 2) นางสาวนัทธมน บุญนิธิ  6201012620139
#----------------------------------------------------------------------------------------------#
import pygame
import sys

pygame.init()
pygame.font.init()

black = (0,0,0)
red = (161, 0, 0)
white = (250,250,250)

text_font1 = pygame.font.Font('freesansbold.ttf', 80)
text_font2 = pygame.font.Font('freesansbold.ttf', 30)

pygame.display.set_caption('One Touch')
screen = pygame.display.set_mode((1000, 700))
surface =pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.fill(black)

#picture bg
image = pygame.image.load(r'C:\software\game\ball.jpg') 

#draw button
def draw_rect(color,rect):
    pygame.draw.rect(screen, color , rect)

#show text
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
    
################################# Final Score ##############################################
screen.blit(image, (200, 400))
text_show('ONE TOUCH')
score_text = create_text('SCORE : ',350,250)
restart_button = pygame.draw.rect(screen, red , (400,380,200,100)) #(left,top,width,hight)
restart_text = create_text('RESTART !',500,440)


clock = pygame.time.Clock()
running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
    screen.blit(surface,(0,0))
    pygame.display.update()
