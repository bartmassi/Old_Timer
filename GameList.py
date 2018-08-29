#Features to add:
# combine the "played" list and the "current game" variable, such that you look at the topmost recently played game
# add games, remove exactly  matching game
1

from random import shuffle
from copy import copy

class GameList:
    def __init__(self,floc):
        with open(floc) as f:
            self.games = f.readlines();
            self.games = map(lambda s: s.strip(),self.games);
            self.played = [];
            self.nplayed = 0;
            
    def getGames(self):
        return list(self.games);
        
    def getPlayed(self):
        return list(self.played);
        
    def getLastPlayed(self):
        if(self.nplayed>0):
            return copy(self.played[self.nplayed-1]);
        else:
            return "No games played!"
            
    def chooseGame(self):
        shuffle(self.games)
        if(self.games):
            self.nplayed += 1;
            self.played.append(self.games.pop());
            return copy(self.played[self.nplayed-1]);
        else:
            return "Game list empty!!!"
            
    def addGame(self,newgame):
        self.games.append(newgame);
        shuffle(self.games)
        return

    def reshuffleLastPlayed(self):
        if(self.nplayed==0):
            return
        self.games.append(self.played.pop());
        self.nplayed -= 1;
        shuffle(self.games);
        return;
        
    def reshuffleNthGame(self,n):
        if(self.nplayed==0):
            return;
        self.games.append(self.played.pop(n))
        self.nplayed -= 1;
        shuffle(self.games);
        return; 
    
    def reset(self):
        self.games = self.games+self.played;
        self.played = [];
        self.nplayed = 0;
        shuffle(self.games)
        return
        