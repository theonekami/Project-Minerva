import pygame,sys
from pygame.locals import *
import Button_class
import minerva,lib
 

def button_init():
    play=Button_class.Button("imgs/play.png",218,300)
    Lib=Button_class.Button("imgs/lib_open.png",0,0)
    Lib.bind(minerva.lib_open)
    return [play,Lib]

def get_data(x):
    load(x)

def load(x=None):
    if(x):
        pygame.mixer.music.load("C:/Users/Kevin Selvan/Music/Music/" + str(x))
        pygame.mixer.music.play()
##
##def now_playing():
##    
##

def main():
    pygame.mixer.pre_init(44100,-16,2,2048)
    pygame.mixer.init()
    pygame.init()
    buttons= button_init()
    DISP= pygame.display.set_mode((500,400))
    load()
    while True:
        for e in pygame.event.get():
            if(e.type== QUIT):
                pygame.quit()
                sys.exit()
            for j in buttons:
                j.update(e)
        for i in buttons:
            i.place(DISP)
        pygame.display.update()
