# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 21:14:26 2014

@author: B
"""

import GameList as gl

def displaylist(l):
    nl = len(l)
    for i in xrange(0,nl):
        print str(i)+": " + str(l[i])

floc = 'C:\\Users\\bartm\\Desktop\\games.txt';
a = gl.GameList(floc);
flag = 1

n = len(a.getGames())
while(flag):
    output = "\nChoose next action (current game:" + a.getLastPlayed() + ", " + str(n) +" games left):\n"+\
        "\t1: Choose next game\n"+\
        "\t2: Reshuffle last game\n"+\
        "\t3: Reshuffle nth game\n"+\
        "\t4: Display unplayed games\n"+\
        "\t5: Display played games\n"+\
        "\t6: Add game\n"+\
        "\t0: Reset tournament\n"+\
        "\to: Quit\n"
    print output
    userin = raw_input().strip();
    if(userin=="1"):
        cg = a.chooseGame();
        n = len(a.getGames());
        print "\nYou got: " + cg;
    elif(userin=="2"):
        a.reshuffleLastPlayed()
        n = len(a.getGames());
    elif(userin=="3"):
        print "\n-------------Played games:"
        displaylist(a.getPlayed())
        print "\nPlease select the number of the game to shuffle."
        resin = raw_input().strip();
        try:
            resin = int(resin)
            if(resin<len(a.getPlayed()) and resin>=0):
                print "Reshuffling \"" + a.getPlayed()[resin] + "\".\n";
                a.reshuffleNthGame(resin);
            else:
                print "\"" + str(resin) + "\" is an invalid input. Returning to menu.\n"
        except:
            print "Input not recognized. Returning to menu.\n";
        n = len(a.getGames());
    elif(userin=="4"):
        print "\n-------------Remaining games:"
        displaylist(a.getGames());
        print "\n\n"
    elif(userin=="5"):
        print "\n-------------Played games:"
        displaylist(a.getPlayed());
    elif(userin=="6"):
        print "Which game would you like to add?\n"
        gamein = raw_input().strip();
        print "Are you sure you would like to add \"" + gamein + "\"? [y/n]\n"
        gameconfirm = raw_input().strip();
        if(gameconfirm.upper()=="Y"):
            a.addGame(gamein);
        elif(gameconfirm.upper()=="N"):
            print "Game not added.\n";
        else:
            print "Input not recognized. Returning to menu.\n"
        n = len(a.getGames());
    elif(userin=="0"):
        print "Are you sure you would like to reset the tournament? [y/n]\n"
        resetin = raw_input().strip();
        if(resetin.upper()=="Y"):
            print "\n Tournament resetting...\n"
            a.reset();
            n = len(a.getGames())
            cg = "none"
        else:
            print "\n Tournament was not reset.\n";
    elif(userin=="o"):
        print "\nTo end the tournament, talk to Bart!"
        #print "\nGoodbye!"
        #flag = 0;
        flag = 1;
    else:
        print "\nInput not recognized."