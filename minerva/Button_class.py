import pygame
from pygame.locals import *


def check():
    return pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],0,0)

class Button:
    def __init__(self,location, x=0, y=0):
        self.img=pygame.image.load(location)
        self.rect=self.img.get_rect()
        self.x=x
        self.y=y
        self.func=None

    def place(self,disp):
        disp.blit(self.img, (self.x,self.y))


    def update(self,event):
        if(event.type==MOUSEBUTTONDOWN and self.rect.contains(check()) and self.func):
           self.func()

    def bind(self, func):
        self.func=func
