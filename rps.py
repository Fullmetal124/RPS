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
    

def singleplayer():
    player1win=0
    aiwin=0
    var=input("what is your name: ")
    player=CPU.waponplr()
    ai=random.randint(1,3)
    winner =CPU.kombat(player, ai)
    if winner == 'player1':
        player1win=player1win+1
    elif winner == 'player2':
        aiwin=aiwin+1
    elif winner == 'tie':
        player1win=player1win+1
        aiwin=aiwin+1
    
    wintotalply = str(player1win)
    wintotalai = str(aiwin)
    print ("The score is "+ var +": "+ wintotalply + " And AI has: " + wintotalai)
    var2=input("Do you want to play again? Y for yes, N no.")
    if var2 == 'y':
        singleplayer()
    if var2 == "n":
        rockmenu()


def multiplayer():
    player1win = 0
    player2win = 0
    var=input("what is player 1 name: ")
    var2=input("what is player 2 name: ")
    player1=CPU.waponplr()
    player2=CPU.waponplr()
    winner =CPU.kombat(player1,player2)
    if winner == 'player1':
        player1win=player1win+1
    elif winner == 'player2':
        player2win=player2win+1
    elif winner == 'tie':
        player1win=player1win+1
        player2win=player2win+1
    wintotalply1 = str(player1win)
    wintotalply2 = str(player2win)
    print ("The score is: "+ var +" has: "+ wintotalply1 +" And "+ var2 +" has: " + wintotalply2)
    var3=input("Do you want to play again? Y for yes, N no.")
    if var3 == 'y':
        multiplayer()
    if var3 == "n":
        rockmenu()

rockmenu()