#!/usr/bin/python3

##This is janky and I'm only a little sorry

import descriptions
from gameutils import *
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print("---------------------------")
    print(rooms[currentRoom]["description"])
    if "item_desc" in rooms[currentRoom]:
        print(rooms[currentRoom]["item_desc"])
    print("---------------------------")

# establish some initial game conditions
# room descriptions contain items in the room, and directions you can go
rooms = descriptions.roomdescr()
ends = descriptions.endings()
upstairs_rooms = ["Library", "Hallway", "Bedroom", "Office", "Garden"]
downstairs_rooms = ["Foyer", "Kitchen", "Living Room", "Garden"]
currentRoom = "Kitchen"
corporeal = False
huntersAwake = False
inventory = []

# display the opening screen
gameOpening()

#=============
#The Game Loop
#=============
while True:
    showStatus()

    # the player MUST type something in, otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:       
    move = move.lower().split(" ", 1)

    #===========
    #GO commands
    #===========

    if move[0] == 'go':
        if move[1]:
            move[1] = move[1].strip()
        #check that their current room contains that direction
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #can't go to heaven
        elif currentRoom in upstairs_rooms and move[1] == "up":
            print("No, that's not the place for you.")
        #not ready for h-e-double-hockey-sticks
        elif currentRoom in downstairs_rooms and move[1] == "down":
            print("No, you're not ready to go there yet.")
        #invalid move
        else:
            print('You can\'t go that way!')

        #specific movement outcomes while you are a ghost
        if corporeal is False:
            if currentRoom == "Garden":
                if "candles" in inventory:
                    #if you move into the garden and you have the candles but don't know the ritual
                    if "tome" not in inventory:
                        print("I have the fire, but what is the chant?")
                    #if you move into the garden with the candles and knowing the ritual
                    else:
                        descriptions.getyabodyback()
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
                if "candles" not in inventory and "tome" in inventory:
                    print("I know the chant, but how can I get fire?")
        
        #if you move into the living room for the first time as a ghost
        #if you move into the living room for the first time as a zombie with no knife

    #===========
    #GET commands
    #===========

    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if move[1] in rooms[currentRoom]['items']:
            #if item is KNIFE or BODY (:P) and you are NOT CORPOREAL
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
                    

        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    #===========
    #OTHER commands
    #===========

    if move[0] == "inventory":
        print("Inventory:", inventory)
    
    if move[0] == "help":
        showHelp()

    if move[0] == "spoil":
        spoilers()

    #===========
    #END GAMES
    #===========

    if 'knife' in inventory:
        #endgame v1: if you have the knife and you enter the living room while the ghost hunters are sleeping
        if currentRoom == "Living Room" and huntersAwake == False:
            print(ends[1] + ends[0])
            print("You win! You have reached ending #1/5.")
            break
        #endgame v2: if you have the knife and you enter the Foyer while the ghost hunters are there
        elif currentRoom == "Foyer" and "strangers" in rooms[currentRoom]["items"]:
            print(ends[2] + ends[0])
            print("You win! You have reached ending #2/5.")
            break
        #endgame v3: if you have the knife and you enter any room with the ghost hunters
        elif "item" in rooms[currentRoom]:
            print(ends[3] + ends[0])
            print("You win! You have reached ending #3/5.")
            break
    #endgame v4: if you have a body but no knife and you encounter the ghost hunters
    elif corporeal == True and "items" in rooms[currentRoom]:
        if "strangers" in rooms[currentRoom]["items"]:
            print(ends[4])
            print("You lost! You have reached ending #4/5.")
            break
    #endgame v5: if you encounter the awakened ghost hunters before you have a body
    elif huntersAwake == True and "items" in rooms[currentRoom]:
        if "strangers" in rooms[currentRoom]["items"]:
            print(ends[5])
            print("You lost! You have reached ending #5/5.")
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