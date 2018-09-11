import pygame

class song:
    def __init__(self, k):
        self.name=k
        self.location="C:/Users/Kevin Selvan/Music/Music/" + str(self.name) #i  promise to gods there better be a better way to do this T-T

    def play():
        pygame.mixer.music.load(self.location)6
        pygame.mixer.music.play()

class Playlist:
    def __init__(self):
        self.songlist=[]

    def add(self,s):
        y=song(s)
        self.songlist.append(s)

    def get(self,z):
        for i in self.songlist:
            if i.name==z:
                i.play()
