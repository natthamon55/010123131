#Game Progect : ONE TOUCH (Pygame & Python Arcade)
#Blog Update : https://s6201012620139.blogspot.com/2020/09/one-touch-game-project-010123131.html
#student id : 1)นางสาวหทัยพัทร ชำนินวล 6201012620244 
#             2) นางสาวนัทธมน บุญนิธิ  6201012620139
#----------------------------------------------------------------------------------------------#
'''
###############################################
#------ test class ball w/o pygame.camera -----#
###############################################

import pygame
from ball import ball

scr_w , scr_h = 1000,700

screen = pygame.display.set_mode( (scr_w , scr_h) )
pygame.display.set_caption('test')

obj_ball = ball(screen)
running = True

while running :

    mx , my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if obj_ball.is_collided(mx, my):
                screen = pygame.display.set_mode( (scr_w , scr_h) )         #เหมือนการรีหน้า surfsce ใหม่เพื่อลบบอลออก
                pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
                obj_ball = ball(screen)

    pygame.display.flip()

pygame.quit()
'''



###############################################
#------ test class ball w/ pygame.camera -----#
#------------ click mouse to play ------------#
#--------------- สร้าง function ---------------#
###############################################
import pygame
from ball import ball      
import pygame.camera
import time

clock = pygame.time.Clock()

scr_w , scr_h = 1000,700

screen = pygame.display.set_mode( (scr_w , scr_h) )

pygame.display.set_caption('test')


def open_camera( frame_size=(640,360),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 


def game_play():

    camera = open_camera()

    surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

    obj_ball = ball(surface)             #สร้างบอลลูกแรก

    running = True

    while running :

        clock.tick(1000)

        img = camera.get_image()
        screen.blit( img , (0,0) )  

        mx , my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_ball.is_collided(mx, my):
                    surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )          #เหมือนการรีหน้า surface ใหม่เพื่อลบบอลออก
                    pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
                    obj_ball = ball(surface)                                            #สร้างบอลลูกใหม่
            
        screen.blit( surface, (0,0) )

        pygame.display.flip()

    camera.stop()
    pygame.quit()


game_play()