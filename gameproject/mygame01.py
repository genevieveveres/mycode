#!/usr/bin/python3

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


# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {
            "Garden" : {
                "description" : '''You are in the Garden, though none of the plants
                have a spent of green or a solitary petal on them. \n
                To the south you see the door back into the house.\n
                In front of you, in the center of the garden, you see an obelisk inscribed with the following:\n
                \tBy Fire and Chant
                \tI Bind Thee Back''',
                "south" : "Kitchen",
            },
            "Kitchen" : {
                "description" : '''You are in the Kitchen.\n
                To the north is a door leading to the Garden.\n
                To the south you see the Foyer.\n
                To the east is a beaded curtain, behind which is the Living Room\n''',
                "item_desc" : '''On the kitchen table there are plates, cups, and 
                utensils covered in the remains of a recent meal. \n
                A shiny knife that you don't recognize catches your eye.''',
                "north" : "Garden",
                "south" : "Foyer",
                "east" : "Living Room",
                "up" : "Library",
                "items": ["knife"]
            },
            "Foyer" : {
                "description" : '''The Foyer of the house greets people who come in the
                front door with a glorious chandelier, now covered in cobwebs. \n
                You don't feel the desire to leave the house. The kitchen is to the north.''',
                "north" : "Kitchen",
                "up" : "Office",
            },
            "Living Room" : {
                "description" : '''There is strange equipment piled around the Living Room.\n
                The circle of salt that the strangers were sleeping within \n
                was ruined when they scampered out through the side door, which is \n 
                still ajar. You aren't interested in leaving the house to go after them anyway though. \n
                To the west is the Kitchen.''',
                "west" : "Kitchen",
                "up" : "Bedroom",
                "items": ["exorcists"]
            },
            "Upstairs Hallway" : {
                "description" : '''You are in the Upstairs Hallway. \n
                There are stairs leading back down into the kitchen. \n
                The door to the Bedroom is to the east. \n
                The door to the Library is to the west. \n
                The door to the Office is to the south.\n''',
                "south" : "Office",
                "east" : "Bedroom",
                "west" : "Library",
                "down" : "Kitchen",
            },
            "Bedroom" : {
                "description" : '''You are in the Bedroom. It smells disgusting.\n
                The door to the Upstairs Hallway is to the west''',
                "item_desc" : '''The stench seems to be originating from a lump under the covers on the bed.''',
                "west" : "Hallway",
                "down" : "Kitchen",
                "items": ["body"]
            },
            "Library" : {
                "description" : '''The walls of the Library are lined floor to ceiling with shelves, \n
                and each shelf is crammed with books that have no titles covered in a coat of dust.''',
                "item_desc" : '''You spot a particularly 
                ancient-looking tome under a reading chair by the window.
                ''',
                "east" : "Hallway",
                "down" : "Kitchen",
                "items": ["ancient tome"]
            },
            "Office" : {
                "description" : '''You are in the office. A grand mahogany wood desk sits on the opposite 
                end of the room.''',
                "item_desc" : '''There are a variety of fat candles on either side of the desk, half-melted from \n
                late nights spent working past dark. A few of them are still usable.''',
                "north" : "Hallway",
                "down" : "Foyer",
                "items": ["candles"]
            }


          }

# establish the initial game conditions
currentRoom = "Kitchen"
corporeal = False
knowsRitual = False
exorcistsAwake = False

# display the opening screen
gameOpening()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if the verb is go
    if move[0] == 'go':
        #check that their current room contains that direction
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            
        #can't go to heaven
        elif move[1] == "up":
            print("No, that's not the place for you.")
        #not ready for h-e-double-hockey-sticks
        elif move[1] == "down":
            print("No, you're not ready to go there yet.")
        # if it's a different invalid move
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #if item is KNIFE and you are NOT CORPOREAL
            if (move[1] == "knife") and (corporeal == False):
                print("That.... didn't work... hmmmmm")
            else:
                #add the item to their inventory
                inventory.append(move[1])
                #display a helpful message
                print("You picked up the " + move[1] + ".")
                #delete the item key:value pairs from the room's dictionary
                del rooms[currentRoom]['item']
                del rooms[currentRoom]["item_desc"]
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