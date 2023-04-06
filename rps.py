#-- This Program was developed by Jason Pototsky
#-- 11/12/2013 for Week 4 Assignment 1
#-- For CyberSecurity Pima JTED
#-- Instructor: Jason Pototsky
#------------------------------------- Region Global Variables --------------------------------------------------

#------------------------------------- End Region Global Variables ------------------------------------------------
#------------------------------------- Region Functions -----------------------------------------------------------

#------------------------------------- End Region Functions ----------------------------------------------------------

#------------------------------------- Region Main -------------------------------------------------------------------

#------------------------------------- End Region Main ----------------------------------------------------------------
import random, sys, CPU 
def rockmenu():
    print("hi welcome to rock paper scissors")
    #print("")
    var2=int(input("please select 1 for single player, 2 for multiplayer, 3 to Quit, or 4 for instructions"))
    if var2 == 1:
        singleplayer()
    if var2 == 2:
        multiplayer()
    if var2 == 3:
        sys.exit()
    if var2 == 4:
        print("Rock-Paper-Scissors is a game played to settle disputes between two people. ")
    print("Thought to be a game of chance that depends on random luck similar to flipping coins or drawing straws, ")
    print("the game is often taught to children to help them settle arguments between themselves on their own without adult intervention. ")
    print("However, the game actually can be a game that has an element of skill that requires quick thinking and perceptive reasoning.1")
    print("The game is played with three possible hand signals that represent a rock, paper, and scissors. Due to this version being played via the ")
    print("terminal, we won't be using hand signals.  Rock wins against scissors; paper wins against rock; ")
    print("and scissors wins against paper. If both players throw the same hand signal, it is considered a tie and both players get a point, make sure the other player doesn't see what you've chosen.")
    rockmenu()
    

def singleplayer():
    try:    
        with open('RPSHighScoreSingleplayer.txt','x') as f:
            f.write("Rock Paper Scissors High Scores!\n")
            f.write("\n")
            f.write("Player 1 High score:\n")
            f.write("\n")
            f.write("0\n")
            f.write("\n")
            f.write("CPU High score:\n")
            f.write("\n")
            f.write("0\n")
            f.close()

        
    except:
        print('Highscores detected')
    
    with open('RPSHighScoreSingleplayer.txt','r') as f:
        for i in range(4):
            f.readline()
        hiplayerSwin = int(f.readline().strip())
        for i in range(2):
            f.readline()
        hiplayerCPUwin = int(f.readline().strip())
        hslinesS = f.readlines()

    player1win=0
    aiwin=0
    var=input("what is your name: ")
    player=CPU.waponplr()
    ai=random.randint(1,3)
    winner =CPU.kombat(player, ai)
    if winner == 'player1':
        player1win=player1win+1
        hslinesS[4] = str(player1win+hiplayerSwin), "\n"
        with open('RPSHighScoreSinglepayer.txt','w') as f:
            f.writelines(hslinesS)
    elif winner == 'player2':
        aiwin=aiwin+1
        hslinesS[7] = str(aiwin+hiplayerCPUwin), "\n"
        with open('RPSHighScoreSinglepayer.txt','w') as f:
            f.writelines(hslinesS)
    elif winner == 'tie':
        player1win=player1win+1
        aiwin=aiwin+1
        hslinesS[4] = str(player1win+hiplayerSwin), "\n"
        hslinesS[7] = str(aiwin+hiplayerCPUwin), "\n"
        with open('RPSHighScoreSinglepayer.txt','w') as f:
            f.writelines(hslinesS)
    
    wintotalply = str(player1win)
    wintotalai = str(aiwin)
    print ("The score is "+ var +": "+ wintotalply + " And AI has: " + wintotalai)
    var3=input("Do you want to play again, quit to menu, or view overall high scores (Highscore will boot you back to menu)? Y for yes, N for no, H for highscore")
    if var3.lower() == 'y':
        multiplayer()
    if var3.lower() == "n":
        rockmenu()
    if var3.lower() == "h":
        with open('RPSHighScoreSingleplayer.txt') as f:
            for line in f:
                print(line)
        rockmenu()


def multiplayer():
    try:    
        with open('RPSHighScoreMultiplayer.txt','x') as f:
            f.write("Rock Paper Scissors High Scores!\n")
            f.write("\n")
            f.write("Player 1 High score:\n")
            f.write("\n")
            f.write("0\n")
            f.write("Player 2 High score:\n")
            f.write("\n")
            f.write("0\n")
            f.close()

        
    except:
        print('Highscores detected')

    with open('RPSHighScoreMultiplayer.txt','r') as f:
        for i in range(4):
            f.readline()
        hiplayer1win = int(f.readline().strip())
        for i in range(2):
            f.readline()
        hiplayer2win = int(f.readline().strip())
        hslines = f.readlines()


    player1win = 0
    player2win = 0
    
    var=input("what is player 1 name: ")
    var2=input("what is player 2 name: ")
    player1=CPU.waponplr()
    player2=CPU.waponplr()
    winner =CPU.kombat(player1,player2)
    if winner == 'player1':
        player1win=player1win+1
        hslines[4] = str(player1win+hiplayer1win), "\n"
        with open('RPSHighScoreMultiplayer.txt','w') as f:
            f.writelines(hslines)
    elif winner == 'player2':
        player2win=player2win+1
        hslines[7] = str(player2win+hiplayer2win), "\n"
        with open('RPSHighScoreMultiplayer.txt','w') as f:
            f.writelines(hslines)
    elif winner == 'tie':
        player1win=player1win+1
        player2win=player2win+1
        hslines[4] = str(player1win+hiplayer1win), "\n"
        hslines[7] = str(player2win+hiplayer2win), "\n"
        with open('RPSHighScoreMultiplayer.txt','w') as f:
            f.writelines(hslines)
    wintotalply1 = str(player1win)
    wintotalply2 = str(player2win)
    print ("The score is: "+ var +" has: "+ wintotalply1 +" And "+ var2 +" has: " + wintotalply2)
    var3=input("Do you want to play again, quit to menu, or view overall high scores (Highscore will boot you back to menu)? Y for yes, N for no, H for highscore")
    if var3.lower() == 'y':
        multiplayer()
    if var3.lower() == "n":
        rockmenu()
    if var3.lower() == "h":
        with open('RPSHighScoreMultiplayer.txt') as f:
            for line in f:
                print(line)
        rockmenu()


rockmenu()