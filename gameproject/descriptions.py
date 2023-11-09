def roomdescr():

    rooms = {
            "Garden" : {
                "description" : '''You are in the Garden, though none of the plants have a speck of green or a solitary petal on them.
A crumbling stone wall encircling the garden marks the property line, and you can't see anything beyond the wall through the fog.\n
In front of you, in the center of the garden, you see an obelisk inscribed with the following:
\tB Y F I R E A N D C H A N T
\tI B I N D T H E E B A C K\n
\tTo the south you see the door back into the house.\n''',
                "south" : "Kitchen",
                "items": []
            },
            "Kitchen" : {
                "description" : '''You are in the Kitchen.\n
\tTo the north is a door leading to the Garden.
\tTo the south you see the Foyer.
\tTo the east is a beaded curtain, behind which is the Living Room.''',
                "item_desc" : '''\nOn the kitchen table there are plates, cups, and utensils covered in the remains of a recent meal. 
A shiny knife that you don't recognize catches your eye.''',
                "north" : "Garden",
                "south" : "Foyer",
                "east" : "Living Room",
                "up" : "Library",
                "items": ["knife"]
            },
            "Foyer" : {
                "description" : '''The Foyer of the house greets people who come in the front door with a glorious chandelier, now covered in cobwebs.
You don't feel any desire to leave the house. \n
\tThe kitchen is to the north.
\tThere is a staircase leading up.''',
                "north" : "Kitchen",
                #as a ghost you phase through the floor instead of taking the stairs
                "up" : "Office",
                "items": []
            },
            "Living Room" : {
                "description" : '''There is strange equipment piled around the Living Room, still blaring away. The circle of salt that the strangers 
were sleeping within was ruined when they scampered out through the side door, which is still ajar. You aren't 
interested in leaving the house to go after them anyway though. \n
\tTo the west is the Kitchen.''',
                "west" : "Kitchen",
                "up" : "Bedroom",
                "items": ["strangers"]
            },
            "Hallway" : {
                "description" : '''You are in the Upstairs Hallway. \n
There are stairs leading back down into the Foyer.
The door to the Bedroom is to the east.
The door to the Library is to the west.
The door to the Office is to the south.''',
                "south" : "Office",
                "east" : "Bedroom",
                "west" : "Library",
                "down" : "Foyer",
                "items": []
            },
            "Bedroom" : {
                "description" : '''You are in the Bedroom. It smells disgusting.\n
\tThe door to the Upstairs Hallway is to the west''',
                "item_desc" : '''\nThe stench seems to be originating from a lump under the covers on the bed.''',
                "west" : "Hallway",
                "down" : "Kitchen",
                "items": ["body"]
            },
            "Library" : {
                "description" : '''The walls of the Library are lined floor to ceiling with shelves, 
and each shelf is crammed with books that have no titles covered in a coat of dust. \n
\tThe door to the Upstairs Hallway is to the east.''',
                "item_desc" : '''\nYou spot a particularly ancient-looking tome under a reading chair by the window.''',
                "east" : "Hallway",
                "down" : "Kitchen",
                "items": ["tome"]
            },
            "Office" : {
                "description" : '''You are in the office. A grand mahogany wood desk sits on the opposite end of the room.\n
\tThe door to the Upstairs Hallway is to the north.''',
                "item_desc" : '''\nThere are a variety of fat candles on either side of the desk, half-melted from
late nights spent working past dark. A few of them are still usable.''',
                "north" : "Hallway",
                "down" : "Foyer",
                "items": ["candles"]
            }


          }
    return rooms

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


def endings():
    endings = [
        ''''\n\n 
You continue to haunt your house in this rotting sack forever, until you are nothing but a skeleton, \n\t...then nothing but dust \n\t\t...then nothing but a ghost again.\n\n''',

        '''The are strangers resting in sleeping bags surrounded by a circle of salt on the 
Living Room floor. There is various equipment positioned around the room, but none of it 
makes a sound. The ghost hunters remain asleep and you use the knife to clear them out. ''',

        '''The strangers are back with some new tools to use against you, 
but it's clear they were expecting a ghost.
When they see your newly reinhabited body and the knife in your hands they exchange a look, 
then bolt out the front door behind them before you can catch up to them.
This time, you know they are gone for good.''',

        '''The strangers are back with some new tools to use against you, 
but it's clear they were expecting a ghost.
When they see your newly reinhabited body and the knife in your hands you see the panic in their eyes
You expected your half decomposed body to be slow, but that is not the case, and they 
cannot escape the point of your knife''',

        '''The strangers are back with some new tools to use against you, 
but it's clear they were expecting a ghost.
When they see your newly reinhabited body and the knife in your hands panic briefly flashes through their eyes. 
Without a weapon to fight them off though, they overpower you quickly, and soon enough you are no more.''',

        '''The ghost hunters are back with some new tools to use against you. They point the nozzle
of their strange machine at you, say words that make you glow and burn, and then you are no more. '''
    ]
    return endings