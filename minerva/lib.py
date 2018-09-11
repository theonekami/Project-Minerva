import tkinter
from tkinter import *
import os,sys
import Song



def test_sing():
    x=[]
    for i,j,k in os.walk("C:/Users/Kevin Selvan/Music/Music"):
        x=k
    return x

##SONGS=

##def hl(event):
##    event.widget.config()[]

def lib(f): ##f is the fucntion to be bound
    root=tkinter.Tk() #init meems
    root.winfo_toplevel().title("Minerva")
    ALL= Song.Playlist()
    
    for i in range(1,4): #I summon 3 EMPTY BUTTONS
        y= Button(root,width=10)
        y.grid(row=i,column=0)

## Ugly kami says "IM A DED MAN"
    s=Scrollbar(root)
    
    x=Listbox(root,selectmode=BROWSE,height=20,width=60)
    
    for i in test_sing():
        ALL.add(i)
        x.insert(END,i) #this i need to change....some FUckin how 
        
    x.bind("<Double-Button-1>",f)#so many undos later kms
    x.bind("<Return>",f)
    x.config(yscrollcommand=s.set)
    s.config(command=x.yview)

    search=Entry(root,text="Eneter Search items",width=60)
    
##    geyass bindings FUN AF
    search.grid(row=0, column=1)
    x.grid(row=1, column=1,rowspan=20)
    s.grid(row=1,column=2, rowspan=20,sticky=N+S)

    root.mainloop()
    print("we are out")
    
