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
import random, sys
def rockmenu():
    print("hi welcome to rock paper scissors")
    #print("")
    var2=int(input("please select 1 for single player, or 2 for multiplayer, or 3 to Quit"))
    if var2 == 1:
        singleplayer()
    if var2 == 2:
        multiplayer()
    if var2 == 3:
        sys.exit()
    

def singleplayer():
    player1win=0
    aiwin=0
    var=input("what is your name: ")
    player=waponplr()
    ai=random.randint(1,3)
    winner = kombat(player, ai)
    if winner == 'player1':
        player1win=player1win+1
    elif winner == 'player2':
        aiwin=aiwin+1
    elif winner == 'tie':
        player1win=player1win+1
        aiwin=aiwin+1
    print ("The score is "+ var +": "+ player1win + " And AI has: " + aiwin)
    var2=input("Do you want to play again?")
    if var == 'Y':
        singleplayer()
    if var == "N":
        rockmenu()


def multiplayer():
    var=input("what is player1 name: ")
    var2=input("what is player2 name: ")
