The Old Timer (OT) tournament is one in which competitors face off in randomly selected games. This repository contains a jupyter notebook for analyzing the results of tournaments, and some simple software for handling game selection during the tournament.

================================CODE

GameList.py is a class definition for the object that holds all of the legal games in a given tournament, and keeps track of what has been played. This list is used to instantiate the random-game-without-replacement rule that governs game selection.

OT_Driver.py is a driver for interacting with a GameList object through the command line. This helps the tournament organizer conduct the tournament.

Old_Timer_Analysis.ipynb is an analysis of the existing database of old timer matches. This examines who the best players are, computes player elo, and examines the most commonly played types of games. Check it out!


================================DATA

OldTimer.db is a SQLite database with two tables: Matches and Games

Matches - a list of all matches that have occured in an OT.
player1: the first player in the match
player2: the second player in the match
winner: the person who won the match
game: the game played during the match

Games - a table of games that have been played in an OT.
game: the title of the game
genre: the genre of the game.


