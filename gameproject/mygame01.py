#!/usr/bin/python3

import descriptions
from gameutils import *
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInv():
    print("Inventory:", inventory)

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print("---------------------------")
    print(rooms[currentRoom]["description"])
    if "item_desc" in rooms[currentRoom]:
        print(rooms[currentRoom]["item_desc"])
    print("---------------------------")

def getyabodyback():
    print('''
You enter the garden with the candles and the words for the chant at the top of your mind. 
You arrange the candles in a circle around the obelisk and the second the last one is in place
flames spring from the wick of each candle. 

You recite the words:
    Tuc dna. Em pleh os! Em pleh os! Em pleh os ro morf emac ti erehw kcab luos ym tup!

There is darkness, and cold. Then, you feel... heavy. But you also feel strangely - inhumanley,
perhaps - strong. You throw off the fabric around you, rise out of the bed for the first time
in ... months? years? decades? into the Bedroom. 

Now, there seem to be some unwanted guests around... what to do about them...
    ''')

# room descriptions contain items in the room, and directions you can go
rooms = descriptions.roomdescr()
upstairs_rooms = ["Library", "Hallway", "Bedroom", "Office", "Garden"]
downstairs_rooms = ["Foyer", "Kitchen", "Living Room", "Garden"]

# establish the initial game conditions
currentRoom = "Kitchen"
corporeal = False
knowsRitual = False
exorcistsAwake = False
inventory = []

# display the opening screen
gameOpening()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in, otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:       
    move = move.lower().split(" ", 1)



    #GO commands



    if move[0] == 'go':
        #check that their current room contains that direction
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #can't go to heaven
        elif currentRoom in upstairs_rooms and move[1] == "up":
            print("No, that's not the place for you.")
        #not ready for h-e-double-hockey-sticks
        elif currentRooom in downstairs_rooms and move[1] == "down":
            print("No, you're not ready to go there yet.")
        #invalid move
        else:
            print('You can\'t go that way!')

        #specific movement outcomes while you are a ghost
        if corporeal is False:
            if currentRoom == "Garden":
                if "candles" in inventory:
                    #if you move into the garden and you have the candles but don't know the ritual
                    if knowsRitual is False:
                        print("I have the fire, but what is the chant?")
                    #if you move into the garden with the candles and knowing the ritual
                    else:
                        getyabodyback()
                        #These didn't get teleported with you
                        inventory.remove("candles")
                        inventory.remove("tome")
                        #The body is no longer in the bedroom - it is you
                        del rooms["Bedroom"]['items'][0]
                        del rooms["Bedroom"]["item_desc"]
                        #You can no longer phase through the floor
                        for room in rooms:
                            if "up" in room:
                                del room["up"] 
                            if "down" in room:
                                del room["down"]
                        #You have to use the stairs now
                        rooms["Hallway"]["down"] = "Foyer"
                        rooms["Foyer"]["up"] = "Hallway"

                        #change the state
                        corporeal = True
                        currentRoom = "Bedroom"
                #if you move into the garden and you know the ritual but don't have the candles
                #I DON'T know why the last check corporeal is necessary but apparently it is
                if "candles" not in inventory and knowsRitual is True and corporeal is False:
                    print(corporeal)
                    print("I know the chant, but how can I get fire?")
        
        #if you move into the living room for the first time as a ghost
        #if you move into the living room for the first time as a zombie with no knife



    #GET commands


    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if move[1] in rooms[currentRoom]['items']:
            #if item is KNIFE and you are NOT CORPOREAL
            if (move[1] == "knife" or move[1] == "body") and (corporeal == False):
                print("That.... didn't work... hmmmmm")
            else:
                #add the item to their inventory
                inventory.append(move[1])
                #display a helpful message
                print("You picked up the " + move[1] + ".")
                #delete the item key:value pairs from the room's dictionary
                del rooms[currentRoom]['items'][0]
                del rooms[currentRoom]["item_desc"]

                if move [1] == "tome":
                    print ('''The book responds to your touch and the pages flutter as they flip open to the dead center of the book. You read:
\t There is a dark ritual I have discovered to rehome a spirit back into its earthly body...
\t To perform the ritual, encircle the obelisk with flame, and recite these words:
\t\tTuc dna. Em pleh os! Em pleh os! Em pleh os ro morf emac ti erehw kcab luos ym tup!

... interesting.''')
                    knowsRitual = True

        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    if move[0] == "inventory":
        showInv()
    
    if move[0] == "help":
        showHelp()



## ENDGAMES


    if 'knife' in inventory:
        #endgame v1: if you have the knife and you enter the living room while the exorcists are sleeping
        if currentRoom == "Living Room" and exorcistsAwake == False:
            print('''The are strangers resting in sleeping bags surrounded by a circle of salt on the 
Living Room floor. There is various equipment positioned around the room, but none of it 
makes a sound. The exorcists remain asleep and you use the knife to clear them out. ''')
        #endgame v2: if you have the knife and you enter the Foyer while the exorcists are there
        elif currentRoom == "Foyer" and "items" in rooms[currentRoom]:
            print('''The exorcists are back with some new tools to use against you, 
but it's clear they were expecting a ghost.
When they see your newly reinhabited body and the knife in your hands they exchange a look, 
then bolt out the front door behind them before you can catch up to them.
This time, you know they are gone for good.''')
        #endgame v3: if you have the knife and you enter any room with the exorcists
        elif "item" in rooms[currentRoom]:
            print('''The exorcists are back with some new tools to use against you, 
but it's clear they were expecting a ghost.
When they see your newly reinhabited body and the knife in your hands you see the panic in their eyes
You expected your half decomposed body to be slow, but that is not the case, and they 
cannot escape the point of your knife ''')
        print(''''\n\n 
            You continue to haunt your house in this rotting sack forever, until you are 
nothing but a skeleton, \n\t...then nothing but dust \n\t\t...then nothing but a ghost again.\n\n
            You win!''')
        break
    #endgame v4: if you have a body but no knife and you encounter the exorcists
    elif corporeal == True and "items" in rooms[currentRoom]:
        if "exorcists" in rooms[currentRoom]["items"]:
            print('''The exorcists are back with some new tools to use against you, 
but it's clear they were expecting a ghost.
When they see your newly reinhabited body and the knife in your hands panic briefly flashes through their eyes. 
Without a weapon to fight them off though, they overpower you quickly, and soon enough you are no more.\n
            You lose!''')
            break
    #endgame v5: if you encounter the awake exorcists before you have a body
    elif exorcistsAwake == True and "items" in rooms[currentRoom]:
        if "exorcists" in rooms[currentRoom]["items"]:
            print('''The exorcists are back with some new tools to use against you. They point the nozzle
of their strange machine at you, say words that make you glow and burn, and then you are no more. \n
            You lose!''')
            break




#Things that have to happen yet - 
#When you go into the garden with the candles
    ##Perform the ritual
    ##Move current location to bedroom
    ##Print words related to being in a new place
    ##change description of the room
    ##remove candles from inventory
    ##change corporeal flag

#When you move into the Living Room
    ##If you have body but no knife
        ##Better not disturb them
    ##If you don't have a body
        ##Wake up the exorcists

#When 