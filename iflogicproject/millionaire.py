#!/usr/bin/env python3

import random
import qbanks
import qvalues
import os
import time

valuesList = qvalues.giveValues()
gameslist = qbanks.allgames()

def welcomeScreen():
    os.system('clear')
    print("\n\nWelcome to WHO WANTS TO BE A MILLIONAIRE! \n With your host, Regis Philbin.")
    time.sleep(3)
    os.system('clear')

def pickGame():
    gameNum=random.randint(0, len(gameslist))
    return gameslist[gameNum-1]

def main():
    welcomeScreen()
    theGame= pickGame()

    counter= 1
    winnings= 0

    while (True) and (counter != 16):
        print("Question #" + str(counter) + ", for $" + valuesList[str(counter)]+": "+theGame[str(counter)]["Q"])
        print("\tA: " + theGame[str(counter)]["A"])
        print("\tB: " + theGame[str(counter)]["B"])
        print("\tC: " + theGame[str(counter)]["C"])
        print("\tD: " + theGame[str(counter)]["D"])
        print(f"You can also enter Q to walk away with your current winnings (${winnings})")
        print("")
        print("So, what'll it be?")
        useranswer = input("> ").upper()

        if (useranswer == "Q"): 
            print("Thank you for playing! You won: $" + str(winnings))
            break
        elif (useranswer != "A") and (useranswer != "B") and (useranswer != "C") and (useranswer != "D"):
            print("Please provide a valid answer.")
            time.sleep(1)
            os.system('clear')
        elif (useranswer == theGame[str(counter)]["answer"]):
            winnings= int(valuesList[str(counter)])
            print("CORRECT!")
            counter += 1
        else:
            print("I'm sorry, that's incorrect. The correct answer was "+theGame[str(counter)]["answer"]+". Better luck next time!")
            break
    
    if(counter == 16):
        print("Amazing! You've won the million dollars!")
        print("Fun fact, this game was won by " + theGame["name"] + " on " + theGame["date"] +".")

if __name__ == "__main__":
        main()