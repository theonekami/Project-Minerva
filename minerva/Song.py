import pygame

class song:
    def __init__(self, k):
        self.name=k
        self.location="C:/Users/Kevin Selvan/Music/Music/" + str(self.name) #i  promise to gods there better be a better way to do this T-T

    def play(self):
        pygame.mixer.music.load(self.location)
        pygame.mixer.music.play()

class Playlist:
    def __init__(self):
        self.songlist=[]
        self.current_song=None

    def add(self,s):
        y=song(s)
        self.songlist.append(y)

    def get(self,z):
        for i in self.songlist:
            if i.name==z:
                i.play() ##and now in reasons why kami is stupid
                self.current_song=i
                ##and now in kami's display of ugly code we see a DOuble loop
                for j in range (self.songlist.index(i),len(self.songlist)):
                    try:
                        pygame.mixer.music.queue(self.songlist[j].location)
                    except:
                        print("REEE")
                return
