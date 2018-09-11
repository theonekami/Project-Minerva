import pygame,sys
from pygame.locals import *
import tkinter as Tk
import thread,Music_screen,lib,Song


    
x=""

def songname(event):
    y=event.widget.get("active")
    Music_screen.get_data(y)

def lib_open():
    Menu=thread.Thread(1, "Library",0,lib.lib)
    if(not Menu.is_alive()):
        Menu.start()
    else:
        print("error is thrown :)")
    print("end of lib_open")


def main_run():
    f1=Music_screen.main
    Start=thread.Thread(0,"mainplayloop",0,f1)
    Start.start()

