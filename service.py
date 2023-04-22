import inventory as i
import random

def startgame(count_win:int):
    i.rounds = count_win
    i.allround = 0
    i.pround = 0 ; i.cround = 0
    return str(i.rounds)+" win rounds to win"

def compet(rps):
    gamelog = ""
    p = rps
    choices = ["r","p","s"]
    c = random.choice(choices)
    if p=="r":
        if c=="r":
            i.allround += 1
            gamelog += "draw p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
        elif c=="p":
            i.cround += 1 ; i.allround += 1
            gamelog += "lose p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
        elif c=="s":
            i.pround += 1 ; i.allround += 1
            gamelog += "win p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
    elif p=="p":
        if c=="r":
            i.pround += 1 ; i.allround += 1
            gamelog += "win p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
        elif c=="p":
            i.allround += 1
            gamelog += "draw p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
        elif c=="s":
            i.cround += 1 ; i.allround += 1
            gamelog += "lose p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
    elif p=="s":
        if c=="r":
            i.cround += 1 ; i.allround += 1
            gamelog += "lose p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
        elif c=="p":
            i.pround += 1 ; i.allround += 1
            gamelog += "win p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
        elif c=="s":
            i.allround += 1
            gamelog += "draw p = "+str(i.pround)+" c = "+str(i.cround)+" in round "+str(i.allround)
    else:
        print("Input only r,p,and s")
        i.allround -= 1
    
    
    if i.rounds == 0:
        gamelog = "Enter round to win to start the game"
    elif i.pround == i.rounds:
        i.pround = 0 ; i.cround = 0
        gamelog += " endgame : win end in "+str(i.allround)+" rounds"
        i.rounds = 0
    elif i.cround == i.rounds:
        i.pround = 0 ; i.cround = 0
        gamelog += " endgame : lose end in "+str(i.allround)+" rounds"
        i.rounds = 0
    
    
    return gamelog