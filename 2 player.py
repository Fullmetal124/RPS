def waponplr():
    print("1-3 will = your weapons.  1 = Rock, 2 = Paper, 3 = Scissors ")
    plr = int(input("Player, choose your weapon:"))
    if plr == 1:
        print ('You selected Rock')
        return 1
    if plr == 2:
        print ('You selected Paper')
        return 2
    if plr == 3:
        print ('You selected Scissors')
        return 3
    else:
        print("Seriously bro? Try again")
        waponplr()


player1=waponplr()
player2=waponplr()

def kombat(player1, player2):
    if player1 == player2:
        print("This is a tie")
        return
    elif player1 == 1 and player2 == 2:
        print("Player 2 wins!!")
        return
    elif player1 == 1 and player2 == 3:
        print("Player 1 wins!!")
        return
    elif player1 == 2 and player2 == 1:
        print("Player 1 wins!!")
        return
    elif player1 == 2 and player2 == 3:
        print("Player 2 wins!!")
        return
    elif player1 == 3 and player2 == 1:
        print("Player 2 wins!!")
        return
    elif player1 == 3 and player2 == 2:
        print("Player 1 wins!!")
        return

kombat(player1,player2)
