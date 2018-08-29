#Features to add:
# combine the "played" list and the "current game" variable, such that you look at the topmost recently played game
# add games, remove exactly  matching game
1

from random import shuffle
from copy import copy

#Class that holds the games to be played. 
class GameList:
	
	#Constructor takes a file location. File is a plaintext document
	#in which each line represents a game. 
    def __init__(self,floc):
        with open(floc) as f:
            self.games = f.readlines();
            self.games = map(lambda s: s.strip(),self.games);
            self.played = [];
            self.nplayed = 0;
            
    #Grabs all games.
    def getGames(self):
        return list(self.games);
    
    #Grabs all games that have been played. 
    def getPlayed(self):
        return list(self.played);
    
    #Grabs the most recently played game.    
    def getLastPlayed(self):
        if(self.nplayed>0):
            return copy(self.played[self.nplayed-1]);
        else:
            return "No games played!"
    
    #Chooses a game to be played, and moves it into the played list.        
    def chooseGame(self):
        shuffle(self.games)
        if(self.games):
            self.nplayed += 1;
            self.played.append(self.games.pop());
            return copy(self.played[self.nplayed-1]);
        else:
            return "Game list empty!!!"
    
    #Add a game that wasn't in the file during construction.        
    def addGame(self,newgame):
        self.games.append(newgame);
        shuffle(self.games)
        return
	
	#Reshuffles the last selected game. Useful for dealing with 'resets'
	#during the tournament.
    def reshuffleLastPlayed(self):
        if(self.nplayed==0):
            return
        self.games.append(self.played.pop());
        self.nplayed -= 1;
        shuffle(self.games);
        return;
     
    #Shuffles the game played n steps ago. n=1 is the last game.  
    def reshuffleNthGame(self,n):
        if(self.nplayed==0):
            return;
        self.games.append(self.played.pop(n))
        self.nplayed -= 1;
        shuffle(self.games);
        return; 
    
    #Resets the list to the initial condition.
    def reset(self):
        self.games = self.games+self.played;
        self.played = [];
        self.nplayed = 0;
        shuffle(self.games)
        return
        
