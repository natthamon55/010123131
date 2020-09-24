
import pygame
import random

pygame.init()

class ball():
    def __init__(self,surface):
        position_ball = [ (100,150) , (100,600) , (900,150) , (900,600) ,
                        (100,350) , (900,350) , (500,150) , (500,600)]
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        self.r = 50
        self.color = (r,g,b)
        self.pos = random.choice(position_ball) 
        self.surface = surface
        self.draw = pygame.draw.circle( self.surface, self.color, self.pos, self.r ,0)
        self.surface_size = surface.get_size()

    def is_collided(self,mx, my):
        if self.draw.collidepoint((mx, my)):
            return True
        else : return False